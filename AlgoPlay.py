from tkinter import *
# from tkinter.ttk import *
from tkinter import messagebox
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

rstclicked = False
canvasVisible = True
# list declared with zero elements.
iteration = [0]
loop = 0
index = 0
flag = True


def widgetsDestroy():
    global searchLabel, linearButton, binaryButton, sortLabel, bubbleSortButton, selectionSortButton, insertionSortButton, heapSortButton, mergeSortButton, quickSortButton

    searchLabel.destroy()
    linearButton.destroy()
    binaryButton.destroy()
    sortLabel.destroy()
    bubbleSortButton.destroy()
    selectionSortButton.destroy()
    insertionSortButton.destroy()
    heapSortButton.destroy()
    mergeSortButton.destroy()
    quickSortButton.destroy()
    entry1.destroy()
    startButton.destroy()
    label1.destroy()


def swap(y, i, j):
    if i != j:
        y[i], y[j] = y[j], y[i]


def linearSearchAlgo(y, key):
    global index
    global loop
    global flag
    flag = True
    loop = 0
    index = 0

    for i in y:
        loop += 1
        if i == key:
            # print(k)
            break
        index += 1

    else:
        flag = False
    # messagebox.INFO("LinearSearch","The Number Not Found In Array.")


def binarySearchAlgo(y, key):
    global index
    global loop
    global flag
    flag = True
    loop = 0
    index = 0
    first = 0
    last = len(y) - 1

    while (first <= last and flag):
        loop += 1
        # to get floor number
        mid = (first + last) // 2
        if y[mid] == key:
            index = mid
            break
        else:
            if key < y[mid]:
                last = mid - 1
            else:
                first = mid + 1
    if first > last:
        flag = False


def bubbleAlgo(y):
    if len(y) == 1:
        return

    swapped = True
    for i in range(len(y) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(y) - 1 - i):
            if y[j] > y[j + 1]:
                swap(y, j, j + 1)
                swapped = True
            yield y


def selectionAlgo(y):
    if len(y) == 1:
        return

    for i in range(len(y)):
        # Find minimum unsorted value.
        minVal = y[i]
        minIdx = i
        for j in range(i, len(y)):
            if y[j] < minVal:
                minVal = y[j]
                minIdx = j
            yield y
        swap(y, i, minIdx)
        yield y


def insertionAlgo(y):
    for i in range(1, len(y)):
        j = i
        while j > 0 and y[j] < y[j - 1]:
            swap(y, j, j - 1)
            j -= 1
            yield y


def heapify(y, n, i):
    largest = i
    # leftChild
    l = 2 * i + 1
    # rightChild
    r = 2 * i + 2

    if l < n and y[i] < y[l]:
        largest = l

    if r < n and y[largest] < y[r]:
        largest = r

    if largest != i:
        swap(y, i, largest)
        yield y
        yield from heapify(y, n, largest)

    yield y


def heapAlgo(y):
    n = len(y)

    # maxheap.
    for i in range(n, -1, -1):
        yield from heapify(y, n, i)

    # deleting Data From maxheap
    for i in range(n - 1, 0, -1):
        swap(y, i, 0)
        yield y
        yield from heapify(y, i, 0)


def mergesort(y, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if y[leftIdx] < y[rightIdx]:
            merged.append(y[leftIdx])
            leftIdx += 1
        else:
            merged.append(y[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(y[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(y[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        y[start + i] = sorted_val
        yield y


def mergeAlgo(y, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeAlgo(y, start, mid)
    yield from mergeAlgo(y, mid + 1, end)
    yield from mergesort(y, start, mid, end)
    yield y


def quickAlgo(y, start, end):
    if start >= end:
        return

    pivot = y[end]
    pivotIdx = start

    for i in range(start, end):
        if y[i] < pivot:
            swap(y, i, pivotIdx)
            pivotIdx += 1
        yield y
    swap(y, end, pivotIdx)
    yield y

    yield from quickAlgo(y, start, pivotIdx - 1)
    yield from quickAlgo(y, pivotIdx + 1, end)


def visualizeSearching(x, y, title):
    def resetSearchClicked():
        global canvasVisible
        global rstclicked
        global label3

        rstclicked = False
        if canvasVisible == True:
            canvas.get_tk_widget().destroy()
            label3.destroy()
            canvasVisible = False

    global canvasVisible

    canvasVisible = True
    width = 0.40
    fig = Figure(figsize=(13, 6), dpi=100)
    ax = fig.add_subplot(111)
    rects = ax.bar(x, y, width, color='#5F9F9F', yerr=None)
    # to display the iteration
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    fig.suptitle(title)
    canvas = FigureCanvasTkAgg(fig, root)
    text.set_text("No of Operations: {}".format(loop))

    if flag:
        rects[index].set_color('r')
    elif not flag:
        label3 = Label(root, text='Number Not Found!!!', font=("Helvetica", 18))
        label3.place(x=660, y=10)

    canvas.draw()

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 1,
                '%d' % int(height),
                ha='center', va='bottom')

    canvas.get_tk_widget().pack(expand=1)

    resetserchButton = Button(root, text='Reset', command=resetSearchClicked)
    resetserchButton.place(x=400, y=10)


def visualize(x, y, generator, title):
    def resetClicked():
        global canvasVisible
        global rstclicked
        global label3

        rstclicked = False
        if canvasVisible == True:
            label3.destroy()
            canvas.get_tk_widget().destroy()
            canvasVisible = False

    global canvasVisible
    canvasVisible = True
    # ind = np.arange(length)
    width = 0.40
    fig = Figure(figsize=(13, 6), dpi=100)
    ax = fig.add_subplot(111)
    rects = ax.bar(x, y, width, color='#5F9F9F', yerr=None)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    fig.suptitle(title)
    canvas = FigureCanvasTkAgg(fig, root)  # A tk DrawingArea.

    def updateFig(y, rects, iteration):

        # zip joins x and y coordinates in pairs
        for rect, val in zip(rects, y):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("No of Operations: {}".format(iteration[0]))

    anima = animation.FuncAnimation(fig, func=updateFig,
                                    fargs=(rects, iteration), frames=generator, interval=1,
                                    repeat=False)
    canvas.draw()

    canvas.get_tk_widget().pack(expand=1)

    resetButton = Button(root, text='Reset', command=resetClicked)
    resetButton.place(x=400, y=10)


def linearSearchClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("LinearSearch")
    root.geometry("1000x650+150+20")

    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    label1 = Label(root, text='Number Tobe Search(Max: 100)')
    label1.place(x=180, y=10)

    entry1 = Entry(root)
    entry1.place(x=345, y=10, width=30)

    def startLSrchClicked():
        global rstclicked

        length = int(entry.get())
        key = int(entry1.get())
        if length <= 50 and key <= 100 and rstclicked == False:
            # inserting random integers in array with size 30 from 1 to 100.
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            linearSearchAlgo(y, key)
            visualizeSearching(x, y, "LinearSearch\nTime Complexity: O(n)")
            # print(y)

            rstclicked = True
        # label3 = Label(root, text = length +" "+ key)
        # label3.pack()
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startLSrchClicked)
    startButton.place(x=480, y=10)


def binarySearchClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("BinarySearch")
    root.geometry("1000x650+150+20")

    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    label1 = Label(root, text='Number Tobe Search(Max: 100)')
    label1.place(x=180, y=10)

    entry1 = Entry(root)
    entry1.place(x=345, y=10, width=30)

    def startBSrchClicked():
        global rstclicked
        length = int(entry.get())
        key = int(entry1.get())
        if length <= 50 and key <= 100 and rstclicked == False:
            y = np.array(np.random.randint(1, 101, length))
            y.sort()
            x = np.arange(1, length + 1, 1)
            binarySearchAlgo(y, key)
            visualizeSearching(x, y, "BinarySearch\nTime Complexity: O(log n)")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startBSrchClicked)
    startButton.place(x=480, y=10)


def bubbleSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("BubbleSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)
    # print(label)
    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startBSClicked():
        global rstclicked
        global iteration

        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = bubbleAlgo(y)
            visualize(x, y, generator, "BubbleSort\nTime Complexity: O(n\u00b2)")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startBSClicked)
    startButton.place(x=480, y=10)


def selectionSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("SelectionSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startSSClicked():
        global rstclicked
        global iteration
        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = selectionAlgo(y)
            visualize(x, y, generator, "SelectionSort\nTime Complexity: O(n\u00b2)")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startSSClicked)
    startButton.place(x=480, y=10)


def insertionSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("InsertionSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startInSClicked():
        global rstclicked
        global iteration
        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = insertionAlgo(y)
            visualize(x, y, generator, "InsertionSort\nTime Complexity: O(n\u00b2)")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startInSClicked)
    startButton.place(x=480, y=10)


def heapSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()

    root.title("HeapSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startHSClicked():
        global rstclicked
        global iteration
        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = heapAlgo(y)
            visualize(x, y, generator, "HeapSort\nTime Complexity: O(nlog(n))")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startHSClicked)
    startButton.place(x=480, y=10)


def mergeSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()

    root.title("MergeSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startMSClicked():
        global rstclicked
        global iteration
        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = mergeAlgo(y, 0, length - 1)
            visualize(x, y, generator, "MergeSort\nTime Complexity: O(nlog(n))")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startMSClicked)
    startButton.place(x=480, y=10)


def quickSortClicked():
    widgetsDestroy()
    global label1
    global startButton
    global entry1

    entry1.destroy()
    startButton.destroy()
    label1.destroy()
    root.title("QuickSort")
    root.geometry("1000x650+150+20")
    label = Label(root, text='Array Size(Max: 50) ')
    label.place(x=20, y=10)

    entry = Entry(root)
    entry.place(x=130, y=10, width=30)

    def startQSClicked():
        global rstclicked
        global iteration
        iteration[0] = 0
        length = int(entry.get())
        if length <= 50 and rstclicked == False:
            y = np.random.randint(1, 101, length)
            x = np.arange(1, length + 1, 1)
            generator = quickAlgo(y, 0, length - 1)
            visualize(x, y, generator, "QuickSort\nTime Complexity: O(n\u00b2)")
            rstclicked = True
        else:
            messagebox.showerror("Error", "Input is Invalid OR press Reset Button.")

    startButton = Button(root, text='Start', command=startQSClicked)
    startButton.place(x=480, y=10)


root = Tk()

root.title("AlgoPlay")
# root.geometry("1000x650+150+20")
root.state('zoomed')
root.iconbitmap('images/logo.ico')

linearPhoto = PhotoImage(file="images/Linear_shadow.png")
binaryPhoto = PhotoImage(file="images/Binary_shadow.png")
bubblePhoto = PhotoImage(file="images/Bubble_shadow.png")
selectionPhoto = PhotoImage(file="images/Selection_shadow.png")
insertionPhoto = PhotoImage(file="images/Insertion_shadow.png")
heapPhoto = PhotoImage(file="images/Heap_shadow.png")
mergePhoto = PhotoImage(file="images/Merge_shadow.png")
quickPhoto = PhotoImage(file="images/Quick_shadow.png")

# global objects
entry1 = Entry(root)
startButton = Button(root, text='')
label1 = Label(root, text='')
label3 = Label(root, text='', font=("Helvetica", 18))

searchLabel = Label(root, text='Searching Algorithm', font=('Comic Sans MS', 20), fg='black')
searchLabel.place(x=20, y=10)

linearButton = Button(root, image=linearPhoto, command=linearSearchClicked, border=0, height=190, width=341)
linearButton.place(x=20, y=50)

binaryButton = Button(root, image=binaryPhoto, command=binarySearchClicked, border=0, height=190, width=341)
binaryButton.place(x=400, y=50)

sortLabel = Label(root, text='Sorting Algorithm', font=('Comic Sans MS', 20), fg='black')
sortLabel.place(x=20, y=260)

bubbleSortButton = Button(root, image=bubblePhoto, command=bubbleSortClicked, border=0, height=190, width=341)
bubbleSortButton.place(x=20, y=300)

selectionSortButton = Button(root, image=selectionPhoto, command=selectionSortClicked, border=0, height=190, width=341)
selectionSortButton.place(x=400, y=300)

insertionSortButton = Button(root, image=insertionPhoto, command=insertionSortClicked, border=0, height=190, width=341)
insertionSortButton.place(x=780, y=300)

heapSortButton = Button(root, image=heapPhoto, command=heapSortClicked, border=0, height=190, width=341)
heapSortButton.place(x=20, y=500)

mergeSortButton = Button(root, image=mergePhoto, command=mergeSortClicked, border=0, height=190, width=341)
mergeSortButton.place(x=400, y=500)

quickSortButton = Button(root, image=quickPhoto, command=quickSortClicked, border=0, height=190, width=341)
quickSortButton.place(x=780, y=500)

menu = Menu(root)
root.config(menu=menu)

Searchmenu = Menu(menu)
Searchmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Searching', menu=Searchmenu)
Searchmenu.add_command(label='Linear Search', command=linearSearchClicked)
Searchmenu.add_command(label='Binary Search', command=binarySearchClicked)

Sortmenu = Menu(menu)
Sortmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Sorting', menu=Sortmenu)
Sortmenu.add_command(label='BubbleSort', command=bubbleSortClicked)
Sortmenu.add_command(label='SelectionSort', command=selectionSortClicked)
Sortmenu.add_command(label='InsertionSort', command=insertionSortClicked)
Sortmenu.add_command(label='HeapSort', command=heapSortClicked)
Sortmenu.add_command(label='MergeSort', command=mergeSortClicked)
Sortmenu.add_command(label='QuickSort', command=quickSortClicked)

root.mainloop()