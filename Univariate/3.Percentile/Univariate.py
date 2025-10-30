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

    def Univariate(dataset,Quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","Q1-25%","Q2-50%","Q3-75%","Q4-100%","IQR","1.5-Value","Lesser","Greater",
                                        "Min","Max"], columns=Quan)
        for columnName in Quan:
            descriptive[columnName]["Mean"]=float(dataset[columnName].mean())
            descriptive[columnName]["Median"]=float(dataset[columnName].median())
            descriptive[columnName]["Mode"]=float(dataset[columnName].mode()[0])
            descriptive[columnName]["Q1-25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2-50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3-75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4-100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3-75%"]-descriptive[columnName]["Q1-25%"]
            descriptive[columnName]["1.5-Value"]=1.5*descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1-25%"]-descriptive[columnName]["1.5-Value"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3-75%"]+descriptive[columnName]["1.5-Value"]
            descriptive[columnName]["Min"]=descriptive[columnName].min()
            descriptive[columnName]["Max"]=descriptive[columnName].max()
        return descriptive