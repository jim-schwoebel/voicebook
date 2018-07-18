import os, getpass, time, sys
import pyautogui

#check version of python to train model in models folder 
g=sys.version
g=g[0]

if g=='2':
    
    library='pyaudioanalysis'

    os.chdir('/Users/'+getpass.getuser()+'/'+library)

    import audioTrainTest as aT

    #now get the folder names that you want to classify 
    modelname=raw_input('what is the name of your model?')
    classnum=raw_input('how many classes are you training? (note only supports N=2 and N=5 classes)')
    a=0
    folderlist=list()
    while a != int(classnum):
        folderlist.append(raw_input('what is the folder name for class %s?'%(str(a+1))))
        a=a+1

elif g=='3':

    library='pyaudioanalysis3'

    os.chdir('/Users/'+getpass.getuser()+'/'+library)

    import audioTrainTest as aT

    #now get the folder names that you want to classify 
    modelname=input('what is the name of your model?')
    classnum=input('how many classes are you training? (note only supports N=2 and N=5 classes)')
    a=0
    folderlist=list()
    while a != int(classnum):
        folderlist.append(input('what is the folder name for class %s?'%(str(a+1))))
        a=a+1

#change directory so images get saved there
try:
    os.chdir('/Users/'+getpass.getuser()+'/'+library+'/models/')
except:
    os.mkdir('/Users/'+getpass.getuser()+'/'+library+'/models/')
    os.chdir('/Users/'+getpass.getuser()+'/'+library+'/models/')

#now make the models around the length of the directory
try:
    if len(folderlist)==2:
        #make folders 
        folder1='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[0]
        folder2='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[1]
                          
        print('training SVM')
                          
        aT.featureAndTrain([folder1,folder2], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", os.getcwd()+'/'+modelname+"_svm2Classes", True)
        time.sleep(3)
        im = pyautogui.screenshot(modelname+'_svm2Classes.png')

        print('training knn')
                          
        aT.featureAndTrain([folder1,folder2], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", os.getcwd()+'/'+modelname+"_knn2Classes", True)
        time.sleep(3)
        im = pyautogui.screenshot(modelname+'_knn2Classes.png')

        print('training extratrees')
                          
        aT.featureAndTrain([folder1,folder2], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", os.getcwd()+'/'+modelname+"_et2Classes", True)
        time.sleep(3)
        im = pyautogui.screenshot(modelname+'_et2Classes.png')

        print('training gradientbost')
                              
        aT.featureAndTrain([folder1,folder2], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", os.getcwd()+'/'+modelname+"_gb2Classes", True)
        time.sleep(3)
        im = pyautogui.screenshot(modelname+'_gb2Classes.png')

        print('training random forest')
                          
        aT.featureAndTrain([folder1,folder2], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", os.getcwd()+'/'+modelname+"_rf2Classes", True)
        time.sleep(3)
        im = pyautogui.screenshot(modelname+'_rf2Classes.png')

        #now manually select the most accurate model from screenshots (can automate this with tesseler)
                          
    elif len(folderlist)==3:
        folder1='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[0]
        folder2='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[1]
        folder3='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[2]

        print('training SVM')
                          
        aT.featureAndTrain([folder1,folder2,folder3], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", modelname+"_svm3Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_svm3Classes.png")

        print('training KNN')

        aT.featureAndTrain([folder1,folder2,folder3], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", modelname+"_knn3Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_knn3Classes.png")

        print('training extratrees')

        aT.featureAndTrain([folder1,folder2,folder3], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", modelname+"_et3Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_et3Classes.png")

        print('training gradientboost')

        aT.featureAndTrain([folder1,folder2,folder3], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", modelname+"_gb3Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_gb3Classes.png")

        print('training random forest')

        aT.featureAndTrain([folder1,folder2,folder3], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", modelname+"_rf3Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_rf3Classes.png")
                          
    elif len(folderlist)==4:
        folder1='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[0]
        folder2='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[1]
        folder3='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[2]
        folder4='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[3]

        print('training SVM')
                          
        aT.featureAndTrain([folder1,folder2,folder3,folder4], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", modelname+"_svm4Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_svm4Classes.png")

        print('training KNN')

        aT.featureAndTrain([folder1,folder2,folder3,folder4], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", modelname+"_knn4Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_knn4Classes.png")

        print('training extratrees')

        aT.featureAndTrain([folder1,folder2,folder3,folder4], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", modelname+"_et4Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_et4Classes.png")

        print('training gradientboost')

        aT.featureAndTrain([folder1,folder2,folder3,folder4], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", modelname+"_gb4Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_gb4Classes.png")

        print('training random forest')

        aT.featureAndTrain([folder1,folder2,folder3,folder4], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", modelname+"_rf4Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_rf4Classes.png")

    elif len(folderlist)==5:
        folder1='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[0]
        folder2='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[1]
        folder3='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[2]
        folder4='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[3]
        folder5='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[4]

        print('training SVM')
                          
        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", modelname+"_svm5Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_svm5Classes.png")

        print('training KNN')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", modelname+"_knn5Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_knn5Classes.png")

        print('training extratrees')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", modelname+"_et5Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_et5Classes.png")

        print('training gradientboost')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", modelname+"_gb5Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_gb5Classes.png")

        print('training random forest')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", modelname+"_rf5Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_rf5Classes.png")

    elif len(folderlist)==6:
        folder1='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[0]
        folder2='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[1]
        folder3='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[2]
        folder4='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[3]
        folder5='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[4]  
        folder6='/Users/'+getpass.getuser()+'/'+library+'/models/'+folderlist[5]

        print('training SVM')
                          
        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5,folder6], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", modelname+"_svm6Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_svm6Classes.png")

        print('training KNN')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5,folder6], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "knn", modelname+"_knn6Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_knn6Classes.png")

        print('training extratrees')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5,folder6], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "extratrees", modelname+"_et6Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_et6Classes.png")

        print('training gradientboost')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5,folder6], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "gradientboosting", modelname+"_gb6Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_gb6Classes.png")

        print('training random forest')

        aT.featureAndTrain([folder1,folder2,folder3,folder4,folder5,folder6], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "randomforest", modelname+"_rf6Classes")
        time.sleep(3)
        im = pyautogui.screenshot(modelname+"_rf6Classes.png")

    else:
        print('Sorry, cannot train 7 or more classes. Please try again with fewer classes')
except:
    
    print('error, folders do not exist or files or improperly formatted')

    
