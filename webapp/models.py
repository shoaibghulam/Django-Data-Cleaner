from django.db import models

# Create your models here.
class Sheet(models.Model):
    sheetId=models.AutoField(primary_key=True)
    sheetName=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.sheetName

class SheetInfo(models.Model):
    infoId=models.AutoField(primary_key=True)
    infoName=models.TextField(max_length=900)
    sheetId=models.ForeignKey(Sheet,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.infoName

class SheetData(models.Model):
    dataId=models.AutoField(primary_key=True)
    dataTitle=models.CharField(max_length=200)
    sheetId=models.ForeignKey(Sheet,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.dataTitle