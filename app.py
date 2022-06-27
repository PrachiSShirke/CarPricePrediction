from flask import  Flask, render_template , request
import pickle
app= Flask(__name__);

@app.route("/")
def Hello():
    return render_template("index.html")

@app.route("/sub", methods= ["POST"])
def sub():
    if request.method=="POST":

        fl= open("randomForestModel.pkl","rb");
        model= pickle.load(file=fl)
        CurrentPrice= request.form["CurrentPrice"];
        KmsDriven= request.form["KmsDriven"];
        owners= request.form["owners"];
        Years= request.form["Years"];
        FuelType= request.form["FuelType"];
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=0
        if FuelType=="0" :
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1;
        elif FuelType=="1":
            Fuel_Type_Petrol=1
            Fuel_Type_Diesel=0;
            
        SellerType= request.form["SellerType"];
        Seller_Type_Individual=0;
        if SellerType=="0" :
            Seller_Type_Individual=1
        
        TransmissionType= request.form["TransmissionType"];
        Transmission_Type_Manual=0;
        if TransmissionType=="0" :
            Transmission_Type_Manual=1
        
        ypred= model.predict([[CurrentPrice,KmsDriven,owners,Years,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,
                        Transmission_Type_Manual]])
        return render_template("index.html",PredictedPrice=ypred);

if(__name__=="__main__"):
    app.run(debug=True)