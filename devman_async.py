import time
import curses  # for win: pip install windows-curses

# step4 !!!

"""
def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, '*', curses.A_DIM)
    canvas.refresh()
    #1 кадр. Выводим тусклую звезду * — устанавливаем для текста атрибут 
    #curses.A_DIM                                                        
    time.sleep(2) # ждем 2 секунды
    canvas.addstr(row, column, '*')
    canvas.refresh()
    # 2 кадр. Выводим обычную звезду *
    time.sleep(0.3) #ждем 0.3 секунды
    canvas.addstr(row, column, '*', curses.A_BOLD)
    canvas.refresh()
    #3 кадр. Выводим яркую звезду * — устанавливаем 
    #для текста атрибут curses.A_BOLD
    time.sleep(0.5) #ждем 0.5 секунд
    canvas.addstr(row, column, '*')
    # 2 кадр. Выводим обычную звезду *
    canvas.refresh()
    time.sleep(0.3) #ждем 0.3 секунды

    # После этого анимация начинается сначала. И так в бесконечном цикле.

    canvas.border() # !!! new
    canvas.refresh()
   
    #time.sleep(5)
"""
row01, column01 = (5, 20)
async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        time.sleep(3)

        canvas.refresh() # — чтобы обновить экран и отрисовать звезду

#coroutine = blink(canvas, row01, column01)
coroutine = blink(canvas, row01, column01)

while True:
    coroutine.send(None)
    curses.update_lines_cols()
    #curses.wrapper(draw)


"""  

if __name__ == '__main__':
    
    while True:
        curses.update_lines_cols()
        curses.wrapper(draw)
        #curses.curs_set()
"""
