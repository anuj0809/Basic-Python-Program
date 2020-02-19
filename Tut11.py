sample = ['PEN','PENCIL','ERASER','SCALE']

# PEN AND PECIL AND ERASER AND SCALE

# for item in sample:
#    if item is not 'SCALE':
#        print(item," AND ",end="")
#    else:
#        print(item)

print(" AND ".join(sample))
print(" BUT ".join(sample))