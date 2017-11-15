# python3


with open('/home/common/orchid/mainsite/scripts/genre_list.txt', 'r') as ofi:
	with open('/home/common/orchid/mainsite/scripts/genre_out', 'w') as outfile:
		for line in lines:
			ofi.write(line.title() + '\n')
