#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 0002 15:26
# @Author  : Aries
# @Site    : 加载yaml数据
# @File    : write_user_command.py.py
# @Software: PyCharm
import yaml


class WriteUserCommand:
	def __init__(self):
		pass

	def read_data(self):
		with open("../config/userconfig.yaml") as fr:
			data = yaml.load(fr, Loader=yaml.FullLoader)
			return data

	def get_value(self, key, port):
		data = self.read_data()
		value = data[key][port]
		return value

	def write_data(self, i, device, bp, port):
		data = self.join_data(i, device, bp, port)
		with open("../config/userconfig.yaml", 'a') as fr:
			yaml.dump(data, fr)

	def join_data(self, i, device, bp, port):
		data = {
			'user_info_' + str(i): {
				'deviceName': device,
				'bp': bp,
				'port': port
			}
		}
		return data

	@staticmethod
	def clear_data():
		with open("../config/userconfig.yaml", 'w') as fr:
			fr.truncate()
		fr.close()
		
	def get_file_lines(self):
		data = self.read_data()
		return len(data)


if __name__ == '__main__':
	print(WriteUserCommand().get_value('user_info_1', 'port'))
