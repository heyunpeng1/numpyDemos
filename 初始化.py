import numpy as np
a = np.array([1.,2,3])
# print(a.dtype) #默认是int64,如果数组里有浮点数则默认为float64
#转换浮点类型为int32类型
a = a.astype(np.int32)
# print(a)

#arange范围函数,起点(包含)，终点(不包含)，步数，类型
a = np.arange(1,101,1,np.float32)
# print(a)
a = a.reshape([10,10])
# print(a)

#范围内均予分布 起点(包含)，终点（包含），均予份数
a = np.linspace(1.,10.,100)
# print(a)

# 1代表最小维度行的列数，2代表最小维度行的行数--》2行一列可看成最小单位；3：3个最小单位为第二最小单位，再继续三个第二最小单位为第三最小单位
a = np.indices((3,2,1))
# print(a)

# 全0矩阵
a = np.zeros(shape=(3,4),dtype=float)
# print(a)

# 全1矩阵
#np.ones(shape=(3,4),dtype=float)

# 对角矩阵
a = np.diag([1,2,3])
# print(a)
a = np.diag(np.array([[1,0,0],[0,2,0],[0,0,3]]))
# print(a)

# 幂零矩阵
a = np.eye(3)
# print(a)

#随机函数创建 3,4为size
a = np.random.rand(3,4)
# print(a)
#4:最大数字（不包含）
a = np.random.randint(4,size=(3,4))
# print(a)
#正态分布
a = np.random.randn(3,4)
print(a)
