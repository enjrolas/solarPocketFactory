from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from command.models import Command

from django.utils import timezone

def command(request):
        if request.method == 'POST':
		_command=request.POST.get('command', 'boo')
		_parameter=request.POST.get('parameter',0)
                jsonString=jsonTranslation(_command)
		myCommand = Command(command=_command, statusTimeStamp=timezone.now(), parameter=_parameter, status='queued', commandTimeStamp=timezone.now(), json=jsonString)
                myCommand.save()
                return HttpResponse(_command)
	else:
		return HttpResponse("bite me")

def jsonTranslation(_command):
	jsonStrings=Translation.objects.filter(command=_command)
	if len(jsonStrings)==1:
		jsonString=jsonStrings[0].json
	else:
		jsonString=""
	return jsonString

	


def latestCommand(request):
	if Command.objects.filter(status='queued').order_by('-commandTimeStamp').exists():
		latest=Command.objects.filter(status='queued').order_by('-commandTimeStamp')[0]
		latest.status= "loaded onto pi"
		latest.statusTimeStamp=timezone.now()
		latest.save()
		return render(request, 'latestCommand.html', { 'command': latest})
	else:
		return HttpResponse("queue_empty")

def newCommands(request):
	if Command.objects.filter(status='queued').order_by('-commandTimeStamp').exists():
		latestCommands=Command.objects.filter(status='queued').order_by('-commandTimeStamp')
		for command in latestCommands:
			command.status= "loaded onto pi"
			command.statusTimeStamp=timezone.now()
			command.save()
		return render(request, 'newCommands.html', { 'commands': latestCommands})
	else:
		return HttpResponse("queue_empty")

def interface(request):
	return render(request, 'interface.html')
