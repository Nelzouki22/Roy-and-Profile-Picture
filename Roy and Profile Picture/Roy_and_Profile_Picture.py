# قراءة قيمة L
L = int(input())

# قراءة عدد الصور N
N = int(input())

# معالجة كل صورة
for _ in range(N):
    W, H = map(int, input().split())
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")

