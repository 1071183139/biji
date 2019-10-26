import random
def quicksort(ll):
    #退出条件
    if len(ll)<2:
        return ll
    else:
        piont_index=0
        po=ll[piont_index] #选择基准,小于基准的,大于基准的
        les_part=[i for i in ll[piont_index+1:] if i <=po]
        gret_part=[i for i in ll[piont_index+1:] if i >po]

        #返回合并结果
        return quicksort(les_part)+[po]+quicksort(gret_part)


ll=list(range(10))
random.shuffle(ll)
print(ll)
print(quicksort(ll))