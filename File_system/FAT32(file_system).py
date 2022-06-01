import os
from pyprnt import prnt
# 물리 드라이브를 읽기 전용과 이진모드로 전환
drive = os.open("\\\\.\\PhysicalDrive1", os.O_RDONLY | os.O_BINARY)

#MRB 파티션 테이블  정보 불러오기
def get_mbr(drive_handle):
    mbr = []

    #파티션 테이블  영역을 읽어서
    #저장을 해보자. 파티션 테이블은 446Bytes
    #뒤에 16Bytes식 저장되있음
    #최대 4새의 파티션 테이블이 있음

    # 드라이브 0 바이트로 커서 움직임. SEEK_SET은 시작에서 0만큼  움직인것을 뜻함
    os.lseek(drive_handle, 0, os.SEEK_SET)
    #드라이브를 0번 바이트에서 512바이트 만큼 데이터를 읽음
    raw_data = os.read(drive_handle, 512)

    index = 446
    while index < 510:   #55 AA 스킵해서 512가 아닌 510
        # 16Bytes식 가져옴
        partition_data = raw_data[index: index + 16]

        index += 16

        if partition_data[4] == 0x00:
            continue
        mbr.append({
            "boot flag": partition_data[0],
            "CHS start": partition_data[1:4],
            "part type": partition_data[4],
            "CHS end":   partition_data[5:8],
            "LBA start": int.from_bytes(partition_data[8:12], 'little'),
            "Size in sector": int.from_bytes(partition_data[12:16], 'little')

        })
    return mbr

def get_vbr(drive_handle, lba_start):
    vbr = {}

    os.lseek(drive_handle, lba_start*512, os.SEEK_SET)

    #vbr 섹터를 읽어옴.
    raw_data = os.read(drive_handle, 512)

    # TODO: 필요한 정보들을 딕셔너리 형식으로 정리
    #vbr["???"] = "어떤값"
    vbr["Bytes per sector"] = int.from_bytes(raw_data[11:13], 'little')
    vbr["cluster per sector"] = raw_data[13]
    vbr["reserved sector count"] = int.from_bytes(raw_data[14:16], 'little')
    vbr["Num of fat"] = raw_data[16]
    vbr["hidden sector"] = int.from_bytes(raw_data[28:32], 'little')
    vbr["total sector 32"] = int.from_bytes(raw_data[32:36], 'little')
    vbr["fat size 32"] = int.from_bytes(raw_data[36:40], 'little')
    vbr["root dirctory cluster"] = int.from_bytes(raw_data[44:48], 'little')
    vbr["file system info"] = int.from_bytes(raw_data[48:50], 'little')

    return vbr


def get_fsinfo(drive_handle, fsinfo_sector):
    os.lseek(drive_handle, fsinfo_sector * 512, os.SEEK_SET)
    raw_data = os.read(drive_handle, 512)
    fsinfo = {}


    fsinfo["Num of free cluster"] = int.from_bytes(raw_data[488:492], "little")
    fsinfo["Next free cluster"] = int.from_bytes(raw_data[492:496], 'little')

    return fsinfo

def get_rootdir_entry(drive_handle, rootdir_sector):
    entry =[]

    os.lseek(drive_handle, rootdir_sector * 512, os.SEEK_SET)
    raw_data = os.read(drive_handle, 512)
    index = 0
    while index < 512:
        raw_entry = raw_data[index:index + 32]
        index += 32

        if raw_entry[0] == 0x00:
            break
        if raw_entry[0] == 0xE5:
            continue
            # LFN엔트리╮(일단 무시)
        if raw_entry[11] == 0x0F:
            continue

        entry.append({
            "name": str(raw_entry[0:8], encoding="ascii"),
            "extension": str(raw_entry[8:11], encoding="ascii"),
            "attr": raw_entry[11],

        })
    return entry



mbr = get_mbr(drive)
vbr = get_vbr(drive, mbr[0]["LBA start"])
print(get_mbr(drive))
prnt(get_mbr(drive))
prnt(get_vbr(drive, mbr[0]["LBA start"]))
print(get_vbr(drive, mbr[0]["LBA start"]))

# fsinfo정보 가져오기╮
fsinfo = get_fsinfo(drive,vbr["hidden sector"] + vbr["file system info"])
prnt(fsinfo)

# 루트 디텍터리의 엔트리 가져오기╮
rootdir_entry = get_rootdir_entry(drive,
    vbr["hidden sector"] + vbr["reserved sector count"]
    + vbr["fat size 32"] + vbr["Num of fat"]
)
prnt(rootdir_entry)

print(rootdir_entry)
