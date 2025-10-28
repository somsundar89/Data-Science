class Univariate():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for ColumnName in dataset.columns:
            if dataset[ColumnName].dtype=='O':
                Qual.append(ColumnName)
            else:
                Quan.append(ColumnName)
        return Quan,Qual