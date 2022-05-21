from django.shortcuts import render , HttpResponse ,redirect
from django.contrib.auth import authenticate,login,logout
from django.views import View
import pandas as pd
import re
import sys
from .models import *
from datetime import datetime
from django.contrib import messages



def add_code(numbers):
		num_list = []
		for num in numbers:
			if len (num) == 12 or len (num) == 9:
				if len (num) == 9:
					num_list.append(num)
				else:
					num_list.append(num)
	
		return num_list


class DashboardView(View):
   def get(self,request):
      if request.user.is_authenticated:
         sheetData=Sheet.objects.all().order_by('-pk')
         data ={
            'numberOfSheet':len(sheetData),
            'sheetData':sheetData,
            'totalData':SheetData.objects.all().count()
         }
         return render(request,'dashboard/pages/dashboard.html',data)
      else:
         return redirect('/login')
class UploadView(View):
   
   def get(self,request):
      if request.user.is_authenticated:
         return render(request,'dashboard/pages/upload.html')
      else:
         return redirect('/login')
   
   def post(self,request):
      extraData=list()
      filename = request.FILES['file']
      fName=filename.name.split('.')[0]
      SheetName=Sheet(sheetName=f"{fName} {datetime.now()}")
      SheetName.save()
      # print(SheetName.pk)
     
      try:
         df = pd.read_excel(filename,usecols=[0], names=['colA'])
        
      except Exception as e:
         print(e,"Please enter correct filename.")
         sys.exit()
      
      # drop null
      df_null=df.dropna()
      null_count = len(df) - len(df_null)
      extraData.append(f"{null_count} empty numbers")
      # drop duplicate
      df_duplicate = df_null.drop_duplicates()
      duplicate_count = len(df) - len(df_duplicate)
      extraData.append(f"{duplicate_count} duplicate numbers")
      # #remove special characters

      speciall_df = df_duplicate['colA'].map(lambda x: re.sub(r'\W+', '', str(x)))
      
      count = speciall_df.str.len()
      value_count_dic = count.value_counts().to_dict()

      for key,value in value_count_dic.items():
         extraData.append(f"{value} number with {key} digits")
      

      allCodes= add_code(speciall_df)
      
      bulk_data = list()
      bulk_info = list()
      for info in extraData:
         bulk_info.append(SheetInfo(infoName=info,sheetId=SheetName))

      for x in allCodes:
         bulk_data.append(SheetData(dataTitle=x,sheetId=SheetName))
      
      bulk_data_added = SheetData.objects.bulk_create(bulk_data)  
      bulk_info_added = SheetInfo.objects.bulk_create(bulk_info)  
      
      return HttpResponse(SheetName.pk)

	 

class DataView(View):
   def get(self,request,id):
      if request.user.is_authenticated:
         data={
            'SheetInfo':SheetInfo.objects.filter(sheetId=id),
            'SheetData':SheetData.objects.filter(sheetId=id)
         }
         return render(request,'dashboard/pages/dataview.html',data)
      else:
         return redirect('/login')
class SheetDeleteView(View):
   def get(self,request,id):
      if request.user.is_authenticated:
        data=Sheet.objects.get(pk=id)
        data.delete()
        return redirect('/')
      else:
         return redirect('/login')

class LoginView(View):
   def get(self,request):
    
      return render(request,'dashboard/pages/login.html')
   def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
           messages.success(request,"Please Enter Correct Username and Password")
           return redirect('/login')

class LogOut(View):
   def get(self,request):
      logout(request)
      return redirect('/login')