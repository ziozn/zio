#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 0027 14:31
# @Author  : Aries
# @Site    : 
# @File    : server.py
# @Software: PyCharm
from util.dos_cmd import DosCmd
from util.port import Port
import threading
import time
from util.write_user_command import WriteUserCommand


class Server:

	def __init__(self):
		"""
		获取设备信息
		:return:
		"""
		self.dos = DosCmd()
		self.device_list = self.get_devices()
		self.write_file = WriteUserCommand()

	def get_devices(self):
		devices_list = []
		devices = self.dos.excute_cmd_result('adb devices')
		if len(devices) >= 2:
			for i in devices:
				if 'List' in i:
					continue
				deivces_info = i.split('\t')
				if deivces_info[1] == 'device':
					devices_list.append(deivces_info[0])
			return devices_list
		else:
			return None

	def create_port_list(self, start_port):
		"""
		创建可用端口
		:return:
		"""
		port = Port()
		port_list = port.create_port_list(start_port, self.device_list)
		return port_list

	def create_command_list(self, i):
		"""
		appium -p 4700 -bp 4701 -U 127.0.0.1:62025
		"""

		command_list = []
		appium_port_list = self.create_port_list(4700)
		bootstrap_port_list = self.create_port_list(4900)
		device_list = self.device_list
		command = 'appium -p ' + str(appium_port_list[i]) + ' -bp ' + str(bootstrap_port_list[i]) + ' -U ' + \
			device_list[i] + ' --no-reset --session-override'
		command_list.append(command)
		self.write_file.write_data(i, device_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
		return command_list

	def start_server(self, i):
		start_list = self.create_command_list(i)
		self.dos.excute_cmd(start_list[0])

	def kill_server(self):
		server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
		if len(server_list) > 0:
			self.dos.excute_cmd('taskkill -F -PID node.exe ')

	def main(self):
		self.kill_server()
		self.write_file.clear_data()
		for i in range(len(self.device_list)):
			appium_start = threading.Thread(target=self.start_server, args=(i,))
			appium_start.start()
		time.sleep(30)


if __name__ == '__main__':
	Server().main()

