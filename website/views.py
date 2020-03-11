from django.shortcuts import render

def home(request):
    return render(request,'home.html',{})

def add(request):
    from random import randint
    num_1= randint(0,10)
    num_2= randint(0,10)

    if request.method == "POST":
        anwser = request.POST['anwser']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        #error handling : if no awnser sended
        if not anwser:
            return render(request,'add.html',{
                'anwser':anwser,
                'my_anwser':'Hey! you forgot to fill out the form !',
                'num_1':num_1,
                'num_2':num_2,
                'color':'warning',
            })


        correct_anwser = int(old_num_1)+int(old_num_2)
        if(int(anwser) == correct_anwser):
            my_anwser="Correct! "+old_num_1+" + "+ old_num_2 +" = "+anwser
            color="success"
        else:
            my_anwser="Incorrect! "+old_num_1+" + "+ old_num_2 +" is not "+anwser+ " it is "+str(correct_anwser)
            color="danger"

        return render(request,'add.html',{
            'anwser':anwser,
            'my_anwser':my_anwser,
            "num_1":num_1,
            'num_2':num_2,
            'correct_anwser':correct_anwser,
            'color':color,
            })
    
    return render(request,'add.html',{
        "num_1":num_1,
        'num_2':num_2,
    })


def subtract(request):
    from random import randint
    num_1= randint(0,10)
    num_2= randint(0,10)

    if request.method == "POST":
        anwser = request.POST['anwser']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

                #error handling : if no awnser sended
        if not anwser:
            return render(request,'subtract.html',{
                'anwser':anwser,
                'my_anwser':'Hey! you forgot to fill out the form !',
                'num_1':num_1,
                'num_2':num_2,
                'color':'warning',
            })

        correct_anwser = int(old_num_1)-int(old_num_2)
        if(int(anwser) == correct_anwser):
            my_anwser="Correct! "+old_num_1+" - "+ old_num_2 +" = "+anwser
            color="success"
        else:
            my_anwser="Incorrect! "+old_num_1+" - "+ old_num_2 +" is not "+anwser+ " it is "+str(correct_anwser)
            color="danger"

        return render(request,'subtract.html',{
            'anwser':anwser,
            'my_anwser':my_anwser,
            "num_1":num_1,
            'num_2':num_2,
            'correct_anwser':correct_anwser,
            'color':color,
            })
    
    return render(request,'subtract.html',{
        "num_1":num_1,
        'num_2':num_2,
    })




def multiply(request):
    from random import randint
    num_1= randint(0,10)
    num_2= randint(0,10)

    if request.method == "POST":
        anwser = request.POST['anwser']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

                #error handling : if no awnser sended
        if not anwser:
            return render(request,'multiply.html',{
                'anwser':anwser,
                'my_anwser':'Hey! you forgot to fill out the form !',
                'num_1':num_1,
                'num_2':num_2,
                'color':'warning',
            })

        correct_anwser = int(old_num_1)*int(old_num_2)
        if(int(anwser) == correct_anwser):
            my_anwser="Correct! "+old_num_1+" * "+ old_num_2 +" = "+anwser
            color="success"
        else:
            my_anwser="Incorrect! "+old_num_1+" * "+ old_num_2 +" is not "+anwser+ " it is "+str(correct_anwser)
            color="danger"

        return render(request,'multiply.html',{
            'anwser':anwser,
            'my_anwser':my_anwser,
            "num_1":num_1,
            'num_2':num_2,
            'correct_anwser':correct_anwser,
            'color':color,
            })
    
    return render(request,'multiply.html',{
        "num_1":num_1,
        'num_2':num_2,
    })

def divide(request):
    from random import randint
    num_1= randint(0,10)
    num_2= randint(1,10)

    if request.method == "POST":
        anwser = request.POST['anwser']
        old_num_1 = request.POST['old_num_1']
        old_num_2 = request.POST['old_num_2']

        #error handling : if no awnser sended
        if not anwser:
            return render(request,'divide.html',{
                'anwser':anwser,
                'my_anwser':'Hey! you forgot to fill out the form !',
                'num_1':num_1,
                'num_2':num_2,
                'color':'warning',
            })


        correct_anwser = int(old_num_1)/int(old_num_2)
        if(float(anwser) == correct_anwser):
            my_anwser="Correct! "+old_num_1+" / "+ old_num_2 +" = "+anwser
            color="success"
        else:
            my_anwser="Incorrect! "+old_num_1+" / "+ old_num_2 +" is not "+anwser+ " it is "+str(correct_anwser)
            color="danger"

        return render(request,'divide.html',{
            'anwser':anwser,
            'my_anwser':my_anwser,
            "num_1":num_1,
            'num_2':num_2,
            'correct_anwser':correct_anwser,
            'color':color,
            })
    
    return render(request,'divide.html',{
        "num_1":num_1,
        'num_2':num_2,
    })

