



#n : number of boxes
#w : number of width boxes
def solution(n, w, num):
    out_box=n%w
    direction=((n-1)//w)%2 #0 is right, 1 is left
    
    all_hight=(n-1)//w
    my_hight=(num-1)//w
    answer=all_hight-my_hight
    if out_box==0:answer+=1
    if answer==0:return 1
    my_place=num%w
    my_direction=(num-1)//w % 2 #0 is right, 1 is left
    if direction==my_direction:
        if out_box>=my_place:
            return answer+1
        else:return answer
    else:
        if w-out_box>=my_place:
            return answer+1
        else:return answer

# Example usage: 8 
