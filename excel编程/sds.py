#!/usr/bin/env python
# -*- coding: utf-8 -*-
import openpyxl
wb = openpyxl.Workbook()
ws = wb.active
ws.cell(row=1,column=1) = 'inter'

wb.save('test.xlsx')







