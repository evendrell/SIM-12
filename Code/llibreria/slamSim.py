import sys,os
import curses
from motorEventsDiscrets import motorEventsDiscrets
  
def main():
    # Inicialización manual de unicurses
    stdscr = curses.initscr()  # Inicializa la pantalla
    curses.curs_set(0)  # Oculta el cursor
    stdscr.clear()  # Limpia la pantalla
    stdscr.refresh()  # Actualiza la pantalla
    
    # Obtiene el tamaño de la pantalla
    height, width = stdscr.getmaxyx()

    # Imprime un mensaje en el centro de la pantalla
    message = "Estem a punt d'arrancar la pràctica"
    y = height // 2
    x = (width - len(message)) // 2
    stdscr.addstr(y, x, message)
    stdscr.refresh()

    # Espera a que el usuario presione una tecla
    stdscr.getch()

    # Start colors in unicurses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK,curses.COLOR_WHITE)

    motor=motorEventsDiscrets()
    motor.run(stdscr)
    curses.endwin()
    # Limpieza manual de unicurses
    
    curses.endwin()  # Finaliza la aplicación de curses

if __name__ == "__main__":
    main()
