import os
file = open('./data/kinetics_test.csv','r')
out_file = open('./data/kinetics_test_modefied.csv','w')
for i,line in enumerate(file):
    line = line.strip()
    print(line)
    if i == 0:
        new_line = 'label,{},is_cc\n'.format(line)
        out_file.write(new_line)
    else:
        new_line = 'test_video,{},0\n'.format(line)
        out_file.write(new_line)
print('Done!')
