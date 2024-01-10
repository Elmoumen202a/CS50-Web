from django.shortcuts import render
import markdown
import random

from . import util

def md_convertto_html(title):
    countents = util.get_entry(title)
    markdowner = markdown.Markdown()
    if countents == None:
        return None
    else:
        return markdowner.convert(countents)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    contents = md_convertto_html(title)
    if contents == None:
        return render(
        request, "encyclopedia/entry_error.html",
        {"message_error" :"The entry  does not exist"}
        )
    else:
        return render(
            request, "encyclopedia/entry_exist.html",
            { "title" :title,
            "content": contents
            })

def search_for_items(request):
    if request.method == "POST":
        searchEntry = request.POST['q']
        content = md_convertto_html(searchEntry)
        if content is not None:
            return render(
            request, "encyclopedia/entry_exist.html",
            { "title" :searchEntry,
            "content": content
            })
        else:
            all_searchEntry = util.list_entries()
            listt =[]
            for keyEntery in all_searchEntry:
                if searchEntry.lower() in keyEntery.lower():
                    listt.append(keyEntery)
            return  render(
            request, "encyclopedia/search.html",
            { "listt" :listt,
            })

def newPage(request):
    if request.method == "GET":
        return render( request, "encyclopedia/newPage.html")
    else:
        title = request.POST["title"]
        content = request.POST["content"]
        title_is_exist = util.get_entry(title)

        if title_is_exist is not None:
            return render(request, "encyclopedia/entry_error.html",{
                "message_error" :"The entry  page already exist"})
        else:
            util.save_entry(title, content)
            contents = md_convertto_html(title)
            return render( request, "encyclopedia/entry_exist.html",{ 
                "title" :title,"content": contents})


def edit(request):
    if request.method == "POST": 
        title = request.POST["entryTitle"]
        content = util.get_entry(title)
        return render( request, "encyclopedia/edit.html",{ 
                "title" :title,"content": content})

def saveEdit(request):
    if request.method == "POST": 
        title = request.POST["title"]
        content = request.POST["content"]
        util.save_entry(title, content)

        contents = md_convertto_html(title)
        return render( request, "encyclopedia/entry_exist.html",{ 
            "title" :title,"content": contents})

def randomPage(request):
    all_request = util.list_entries()
    random_request = random.choice(all_request)
    contents = md_convertto_html(random_request)
    return render( request, "encyclopedia/entry_exist.html",{ 
            "title" :random_request,"content": contents})
