import evds as ev
import pandas as pd
import plotly.express as px

#Evds api ile verilerin çekilmesi ve hazırlanması
with open("C:/Users/YUNUS/Desktop/Evds.txt") as dosya:
    api=dosya.read()

evds=ev.evdsAPI(api)

veri=evds.get_data(["TP.ODEMGZS.ALMANYA","TP.ODEMGZS.AVUSTURYA","TP.ODEMGZS.BELCIKA",
                    "TP.ODEMGZS.DANIMARKA","TP.ODEMGZS.FINLANDIYA","TP.ODEMGZS.FRANSA",
                    "TP.ODEMGZS.HOLLANDA","TP.ODEMGZS.INGILTERE"],startdate="01-01-2008",
                    enddate="01-01-2025",frequency=8)

veri.columns=["Yıl","Almanya","Avusturya","Belçika","Danimarka","Finlandiya","Fransa",
              "Hollanda","İngiltere"]

#Melt ile tek sütuna dönüştürme
veri_melt=veri.melt(id_vars="Yıl",var_name="Ülke",value_name="Ziyaretçi Sayısı")

#Grafik kurma
fig=px.bar(veri_melt,x="Ziyaretçi Sayısı",y="Ülke",color="Ülke", 
             animation_frame="Yıl",range_x=[0,veri_melt["Ziyaretçi Sayısı"].max()],
             orientation="h",
             labels={"Ziyaretçi Sayısı":"Ziyaretçi Sayısı","Ülke":"Ülke"}, 
             title="Yıllara Göre Türkiye\'yi Ziyaret Eden Ülke Vatandaşları Sayısı",
             text="Ziyaretçi Sayısı")

fig.update_layout(
    xaxis_title="Ziyaretçi Sayısı", 
    yaxis_title="Ülke", 
    yaxis={"categoryorder":"total ascending"},
    title_font={"size":24,"family":"Arial","color":"black","weight":"bold"},
    title_x=0.5,
    xaxis_title_font={"size":14,"family":"Arial","color":"black","weight":"bold"},
    yaxis_title_font={"size":14,"family":"Arial","color":"black","weight":"bold"},  
    showlegend=False)

fig.update_traces(texttemplate='%{text:,.0f}')

fig.show()


