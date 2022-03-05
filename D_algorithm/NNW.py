import numpy as up
import scipy.special

class NauralNetwark:
    #신경망 초기화
    #입력 노드, 히든노드, 출력노드의 개수와 학습을 초기화하고 가중치(Weight)행렬 생성
    def __init__(self, inputnodes, hiddennodes, outputnodes):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        #가중치 행렬 wih (W of  input -> hidden)
        #가중치 행렬 who (W of hidden -> output)
        #
        
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        
        #주석작성 포기
        self.activation_function = lambda x: scipy.special.expit(x)
        
    def train(self, inputs_list, targets_list, learning_rate):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        
        hidden_layer_in = np.dot(self.wih, inputs)
        hidden_layer_out = self.activation_function(hidden_layer_in)
        output_layer_in = np.dot(self.who, hidden_layer_out)
        output_layer_out = self.activation_function(output_layer_in)
        output_error = targets - output_layer_out
        hidden_error = np.dot(self.who.T, output_error)
        self.who += learning_rate * np.dot((output_error*output_layer_out * (1.0 - output_layer_out)), np.transpose(hidden_layer_out))
        self.wih += learning_rate * np.dot((hidden_error * hidden_layer_out * (1.0 - hidden_layer_out)), np.transpose(input))
    
    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        hidden_layer_in = np.dot(self.wih, inputs)
        hidden_layer_out = self.activation_function(hidden_layer_in)
        out_layer_in = np.dot(self.who, hidden_layer_out)
        out_layer_out = self.activation_function(out_layer_in)
        return out_layer_out
