import bpy
d = bpy.context.active_object.data.archipack_kitchen[0]
bpy.ops.archipack.material(category='kitchen', material='DEFAULT')

d.base_height = 0.10000000149011612
d.base_sink = 0.05000000074505806
d.baseboard = True
d.cabinet_num = 11
d.cabinets.clear()
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '3'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.0
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = True
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 5
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '3'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 11
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '3'
item_sub_1.base_left = True
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '1'
item_sub_2.p0 = (0.31800001859664917, -0.29499998688697815, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.31800001859664917, -0.29499998688697815, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (0.017999999225139618, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.6180000305175781, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.017999999225139618, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.6180000305175781, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.017999999225139618, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.6180000305175781, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = True
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '1'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 1
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '59'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '2'
item_sub_2.p0 = (0.9360000491142273, -0.29499998688697815, 0.862000048160553)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.9360000491142273, -0.29499998688697815, 0.862000048160553)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (0.6360000371932983, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.6360000371932983, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.6360000371932983, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '1'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '11'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 5
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '2'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '6'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '3'
item_sub_2.p0 = (1.5360000133514404, -0.29499998688697815, 0.862000048160553)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.5360000133514404, -0.29499998688697815, 0.862000048160553)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (1.2360000610351562, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.2360000610351562, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.2360000610351562, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '1'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 5
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '3'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '1'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '4'
item_sub_2.p0 = (2.136000156402588, -0.29499998688697815, 0.862000048160553)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.136000156402588, -0.29499998688697815, 0.862000048160553)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (1.8360000848770142, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.8360000848770142, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.8360000848770142, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '1'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '2'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 1
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '1'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '54'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '5'
item_sub_2.p0 = (2.7360000610351562, -0.29499998688697815, 0.862000048160553)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.7360000610351562, -0.29499998688697815, 0.862000048160553)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (2.436000108718872, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (2.436000108718872, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (2.436000108718872, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '1'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.0
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = True
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 5
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '2'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '1'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = True
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '6'
item_sub_2.p0 = (3.3360002040863037, -0.29499998688697815, 0.862000048160553)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.3360002040863037, -0.29499998688697815, 0.862000048160553)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (3.0360002517700195, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (3.0360002517700195, 0.0, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, 0.0, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (3.0360002517700195, -0.6079999804496765, 0.10000000149011612)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.5, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, -0.6079999804496765, 0.10000000149011612)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '2'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.6359999775886536
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 1
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '3'
item_sub_1.base_left = False
item_sub_1.expand = True
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '7'
item_sub_2.p0 = (0.9359999895095825, -0.19499999284744263, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (0.9359999895095825, -0.19499999284744263, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (0.6359999775886536, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.6359999775886536, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (0.6359999775886536, -0.40799999237060547, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.2360000610351562, -0.40799999237060547, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = True
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '2'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 1
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '2'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '8'
item_sub_2.p0 = (1.5360000133514404, -0.19499999284744263, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.5360000133514404, -0.19499999284744263, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (1.2360000610351562, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.2360000610351562, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.2360000610351562, -0.40799999237060547, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (1.8360000848770142, -0.40799999237060547, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '2'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 1
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '3'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '9'
item_sub_2.p0 = (2.136000156402588, -0.19499999284744263, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.136000156402588, -0.19499999284744263, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (1.8360000848770142, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.8360000848770142, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (1.8360000848770142, -0.40799999237060547, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.436000108718872, -0.40799999237060547, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = -0.12700000405311584
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '2'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = False
item_sub_1.baseboard = True
item_sub_1.n_modules = 2
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 1
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '55'
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 5
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '2'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '10'
item_sub_2.p0 = (2.7360000610351562, -0.19499999284744263, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (2.7360000610351562, -0.19499999284744263, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (2.436000108718872, 0.0, 1.624000072479248)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, 0.0, 1.624000072479248)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (2.436000108718872, 0.0, 1.624000072479248)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, 0.0, 1.624000072479248)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (2.436000108718872, -0.40799999237060547, 1.4970000982284546)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.0360002517700195, -0.40799999237060547, 1.4970000982284546)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
item_sub_1 = d.cabinets.add()
item_sub_1.name = ''
item_sub_1.panel_left_width = 0.017999999225139618
item_sub_1.x = 0.6000000238418579
item_sub_1.dz = 0.0
item_sub_1.dy = 0.0
item_sub_1.py = 0.0
item_sub_1.cab_location = '2'
item_sub_1.angle = 0.0
item_sub_1.rotate = '0'
item_sub_1.px = 0.0
item_sub_1.base_sink = 0.05000000074505806
item_sub_1.type = '0'
item_sub_1.counter_x = 0.5
item_sub_1.panel_right = True
item_sub_1.baseboard = True
item_sub_1.n_modules = 1
item_sub_1.panel_right_width = 0.017999999225139618
item_sub_1.counter = '1'
item_sub_1.modules.clear()
item_sub_2 = item_sub_1.modules.add()
item_sub_2.name = ''
item_sub_2.modules = 6
item_sub_2.handle = True
item_sub_2.auto_update = True
item_sub_2.shelves = 1
item_sub_2.z = 0.7620000243186951
item_sub_2.type = '2'
item_sub_1.base_left = False
item_sub_1.expand = False
item_sub_1.auto_update = True
item_sub_1.base_front = 0.0
item_sub_1.base_right = False
item_sub_1.counter_y = 0.4000000059604645
item_sub_1.manipulators.clear()
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = '11'
item_sub_2.p0 = (3.3360002040863037, -0.19499999284744263, 2.131999969482422)
item_sub_2.type_key = 'DUMB_STRING'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-3.0, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.3360002040863037, -0.19499999284744263, 2.131999969482422)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = 'x'
item_sub_2.p0 = (3.0360002517700195, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (-0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (3.0360002517700195, 0.0, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, 0.0, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_2 = item_sub_1.manipulators.add()
item_sub_2.name = ''
item_sub_2.prop1_name = ''
item_sub_2.p0 = (3.0360002517700195, -0.40799999237060547, 1.3700000047683716)
item_sub_2.type_key = 'DUMB_SIZE'
item_sub_2.prop2_name = ''
item_sub_2.p2 = (0.25, 0.0, 0.0)
item_sub_2.normal = (0.0, 0.0, 1.0)
item_sub_2.p1 = (3.636000156402588, -0.40799999237060547, 1.3700000047683716)
item_sub_2.pts_mode = 'SIZE'
item_sub_1.pz = 0.0
item_sub_1.reset_location = False
item_sub_1.lock_p = True
item_sub_1.panel_left = False
d.counter = True
d.counter_chanfer = 0.0010000000474974513
d.counter_y = 0.029999999329447746
d.counter_z = 0.02500000037252903
d.door_board_chanfer = 0.0010000000474974513
d.door_chanfer = 0.0010000000474974513
d.door_gap = 0.001999998465180397
d.door_style = '11'
d.door_x = 0.08000000566244125
d.door_y = 0.017999999225139618
d.handle = '140'
d.handle_dx = 0.05000000074505806
d.handle_dz = 0.1809999942779541
d.handle_fit = False
d.handle_r = 0.09999999403953552
d.handle_space = 0.9300000071525574
d.handle_x = 0.11999999731779099
d.handle_y = 0.03099999949336052
d.handle_z = 0.009999999776482582
d.module_size = 0.12700000405311584
d.modules_default = 6
d.modules_full = 16
d.modules_wall = 6
d.thickness = 0.017999999225139618
d.y = 0.5899999737739563
d.yw = 0.38999998569488525
d.z_default = 0.7620000243186951
d.z_full = 2.0320000648498535
d.z_mode = '1'
d.z_wall = 0.7620000243186951
