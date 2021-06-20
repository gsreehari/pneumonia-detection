from django.http import JsonResponse
from .models import UserData
from fastai.vision import *
from fastai.metrics import *
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
from torchvision.models import resnet50

x = 'C:/Users/Sudarshan/Desktop/pneumonia_detection/pneumonia_detection/model'
path = Path(x)

# from .model
def train(req):
    np.random.seed(40)
    data = ImageDataBunch.from_folder(path, train='.', valid_pct=0.2, ds_tfms=get_transforms(), size=224, num_workers=4).normalize(imagenet_stats)
    learn = cnn_learner(data, resnet50, metrics=[accuracy, error_rate, Precision], model_dir=Path('Path'),
                        path=Path("."))

    lr1 = 1e-3
    lr2 = 1e-1
    learn.fit_one_cycle(2, slice(lr1, lr2))
    learn.save()
    learn.export(".model/model.pkl")

    return JsonResponse({"data": "trained"})


@csrf_exempt
def getResults(request):
    pname = request.POST.get('name')
    age = int(request.POST.get('age'))
    learn = load_learner(x)
    img = open_image(x+"/img4.jpeg")
    pred = learn.predict(img)[0]

    user = UserData.objects.create(name=pname, age=age, image=request.FILES['image'], result=pred)
    res = {}
    res['name'] = pname

    return JsonResponse({'result':str(pred)}, safe=False)