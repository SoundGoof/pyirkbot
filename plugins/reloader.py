# coding: utf-8

from commands import Command
import os
import utility

class ReloadCommand(Command):
	def trig_reload(self, bot, source, target, trigger, argument):
		if utility.has_admin_privileges(source, target):
			bot.reload_plugins()
			bot.reload()
			return "Reloaded and good to go!"
			
class LoadCommand(Command):
	def trig_load(self, bot, source, target, trigger, argument):
		plugin = argument
		if utility.has_admin_privileges(source, target):
			try:
				bot.load_plugin(plugin)
			except ImportError, e:
				return "Unable to load '%s', %s" % (plugin, e)
			return "Plugin %s loaded. Use 'reload' to initialize it." % plugin
