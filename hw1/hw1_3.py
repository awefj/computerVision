import cv2 as cv

cap = cv.VideoCapture('stopwatch.avi')
if not cap.isOpened():
    print('Video open failed')
    exit()
fps = cap.get(cv.CAP_PROP_FPS)
w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
w_2 = int(w/2)
h_2 = int(h/2)
delay = round(1000 / fps)
t_frame = cap.get(cv.CAP_PROP_FRAME_COUNT)

print('width : ', w)
print('height : ', h)
print('fps : ', fps)
print('delay : ', delay)
print('total frame count : ', t_frame)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
output = cv.VideoWriter('stopwatch_inv.avi', fourcc, fps, (w, h))
if not output.isOpened():
    print('file open failed')
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if cap.get(cv.CAP_PROP_POS_FRAMES) > 300 : #초당 30프레임이므로 300프레임 이후는 10초 이후.
        #프레임의 우하단 1/4 부분을 반전
        temp = frame[h_2:h, w_2:w]
        frame[h_2:h, w_2:w] = ~temp

    output.write(frame)

    #cv.imshow('frame', ret)
    cv.imshow('inversed', frame)
    if cv.waitKey(delay) == 27:
        break
cv.destroyAllWindows()