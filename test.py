from _plota import plot

if __name__ == "__main__":
    a = plot()
    a.setx("gmro")
    a.sety("gmoverid")
    a.setlogx(True)
    a.setinvx(True)
    a.setvdsrc([1])
    a.setgateL([1])
    
    print(a.getx())