
import os
import pathlib
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plotAll(x:pd.Series, y:pd.DataFrame, xLabNam:str, yLabNam:str, dataLab:list, saveDir:str, saveNam:str, xDispIval:int=1, \
    xLabFS:int=14, yLabFS:int=14, xTickFS:int=12, yTickFS:int=12, legCol:int=1, legFS:int=10, legLoc:str="best", wFig:float=5, hFig:float=5) -> None:
    
    """
    Function : Create all data's graph in a single figure. The type of an input data is supposed to be pd.DataFrame.

    Args :
        x : Data of x axis
        y : Data of y axis
        xLabNam : Label name of x axis
        yLabNam : Label name of y axis
        dataLab : Label name of legend
        saveDir : Figure save directory's path
        saveNam : Figure save name
        xDispIval : Number of x value display interval
        xLabFS : Fontsize of x label name
        yLabFS : Fontsize of y label name
        xTickFS : Fontsize of x tick
        yTickFS : Fontsize of y tick
        legCol : Number of columns in legend
        legFS : Number to define fontsize of legend
        legLoc : Define location of legend
        wFig : Adjust width-direction figure size
        hFig : Adjust height-direction figure size

    return : None

    """

    # Make directory for saving figure
    os.makedirs(saveDir, exist_ok = True)

    # Create figure in object orient style
    fig, ax = plt.subplots(1, 1, figsize=(wFig, hFig))
    for yDataNum in range(len(dataLab)):
        ax.plot(x, y.iloc[:, yDataNum], label=dataLab[yDataNum])
    ax.set_xlabel(xLabNam, fontsize=xLabFS)
    ax.set_ylabel(yLabNam, fontsize=yLabFS)
    ax.set_xticks(x[::xDispIval]) 
    ax.tick_params(axis='x', labelsize=xTickFS)
    ax.tick_params(axis='y', labelsize=yTickFS)
    ax.legend(ncol=legCol, fontsize=legFS, loc=legLoc)
    ax.grid(linestyle='--', linewidth=0.5)
    fig.savefig(saveDir + saveNam, bbox_inches="tight")
    plt.close()
    return None


def plotEach(x:pd.Series, y:pd.DataFrame, figRowNum:int, figColNum:int, xLabNam:str, dataLab:list, saveDir:str, saveNam:str, xDispIval:int=1, \
    xLabFS:int=12, yLabFS:int=12, xTickFS:int=10, yTickFS:int=10, wPitch:float=0.4, hPitch:float=0.4, wFig:float=7, hFig:float=7, shareX:bool=True, shareY:bool=True) -> None:
    
    """
    Function : Create all data's graph in each figure. The type of an input data is supposed to be pd.DataFrame.

    Args :
        x : Data of x axis
        y : Data of y axis
        figRowNum : Number of figure rows
        figColNum : Number of figure columns
        xLabNam : Label name of x axis
        dataLab : Label name of legend
        saveDir : Figure save directory's path
        saveNam : Figure save name
        xDispIval : Number of x value display interval
        xLabFS : Fontsize of x label name
        yLabFS : Fontsize of y label name
        xTickFS : Fontsize of x tick
        yTickFS : Fontsize of y tick
        wPitch : Adjust width-direction figure pitch
        hPitch : Adjust height-direction figure pitch
        wFig : Adjust width-direction figure size
        hFig : Adjust height-direction figure size
        shareX : Judge whether share x axis or not
        shareY : Judge whether share y axis or not

    return : None

    """

    # Make directory for saving figure
    os.makedirs(saveDir, exist_ok = True)

    # Create figure in object orient style
    fig, axes = plt.subplots(figRowNum, figColNum, sharex=shareX, sharey=shareY, gridspec_kw=dict(wspace=wPitch, hspace=hPitch), figsize=(wFig, hFig))
    rowIdx = 0
    colIdx = 0

    if figRowNum == 1:
        for yDataNum in range(len(dataLab)):
            axes[colIdx].plot(x, y.iloc[:, yDataNum].values)
            axes[colIdx].set_ylabel(dataLab[yDataNum], fontsize=yLabFS)
            axes[colIdx].set_xticks(x[::xDispIval]) 
            axes[colIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[colIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[colIdx].grid(linestyle='--', linewidth=0.5)
            colIdx += 1
        
        fig.text(0.5, 0, xLabNam, ha='center', va='center', fontsize=xLabFS)
        fig.savefig(saveDir + saveNam, bbox_inches="tight")
        plt.close()
        return None

    elif figColNum == 1:
        for yDataNum in range(len(dataLab)):
            axes[rowIdx].plot(x, y.iloc[:, yDataNum].values)
            axes[rowIdx].set_ylabel(dataLab[yDataNum], fontsize=yLabFS)
            axes[rowIdx].set_xticks(x[::xDispIval]) 
            axes[rowIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[rowIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[rowIdx].grid(linestyle='--', linewidth=0.5)
            rowIdx += 1
        
        fig.text(0.5, 0, xLabNam, ha='center', va='center', fontsize=xLabFS)
        fig.savefig(saveDir + saveNam, bbox_inches="tight")
        plt.close()
        return None

    else:
        for yDataNum in range(len(dataLab)):
            axes[rowIdx, colIdx].plot(x, y.iloc[:, yDataNum].values)
            axes[rowIdx, colIdx].set_ylabel(dataLab[yDataNum], fontsize=yLabFS)
            axes[rowIdx, colIdx].set_xticks(x[::xDispIval]) 
            axes[rowIdx, colIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[rowIdx, colIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[rowIdx, colIdx].grid(linestyle='--', linewidth=0.5)
            colIdx += 1
            if colIdx % figColNum == 0:
                rowIdx += 1
                colIdx = 0
            else:
                continue
        
        fig.text(0.5, 0, xLabNam, ha='center', va='center', fontsize=xLabFS)
        fig.savefig(saveDir + saveNam, bbox_inches="tight")
        plt.close()
        return None


def plotEachGroup(x:pd.Series, y:pd.DataFrame, figRowNum:int, figColNum:int, groupNum:int, xLabNam:str, yLabNam:str, dataLab:list, saveDir:str, saveNam:str, xDispIval:int=1, \
    xLabFS:int=14, yLabFS:int=14, xTickFS:int=10, yTickFS:int=10, legCol:int=1, legFS:int=8, legLoc:str="lower right", \
    wPitch:float=0.4, hPitch:float=0.4, wFig:float=7, hFig:float=7, shareX:bool=True, shareY:bool=True) -> None:
    
    """
    Function : Create all data's graph in each figure. The type of an input data is supposed to be pd.DataFrame.

    Args :
        x : Data of x axis
        y : Data of y axis
        figRowNum : Number of figure rows
        figColNum : Number of figure columns
        xLabNam : Label name of x axis
        yLabNam : Label name of y axis
        dataLab : Label name of legend
        saveDir : Figure save directory's path
        saveNam : Figure save name
        xDispIval : Number of x value display interval
        xLabFS : Fontsize of x label name
        yLabFS : Fontsize of y label name
        xTickFS : Fontsize of x tick
        yTickFS : Fontsize of y tick
        legCol : Number of columns in legend
        legFS : Number to define fontsize of legend
        legLoc : Define location of legend
        wPitch : Adjust width-direction figure pitch
        hPitch : Adjust height-direction figure pitch
        wFig : Adjust width-direction figure size
        hFig : Adjust height-direction figure size
        shareX : Judge whether share x axis or not
        shareY : Judge whether share y axis or not

    return : None

    """

    # Make directory for saving figure
    os.makedirs(saveDir, exist_ok = True)

    # Create figure in object orient style
    fig, axes = plt.subplots(figRowNum, figColNum, sharex=shareX, sharey=shareY, gridspec_kw=dict(wspace=wPitch, hspace=hPitch), figsize=(wFig, hFig))
    rowIdx = 0
    colIdx = 0
    count = 0

    if figRowNum == 1:
        for yDataNum in range(len(dataLab)):
            axes[colIdx].plot(x, y.iloc[:, yDataNum].values, label=dataLab[yDataNum])
            axes[colIdx].set_xticks(x[::xDispIval]) 
            axes[colIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[colIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[colIdx].legend(ncol=legCol, fontsize=legFS, loc=legLoc)
            axes[colIdx].grid(linestyle='--', linewidth=0.5)
            count += 1
            if count%groupNum == 0:
                colIdx += 1
                count = 0
            else:
                continue

    elif figColNum == 1:
        for yDataNum in range(len(dataLab)):
            axes[rowIdx].plot(x, y.iloc[:, yDataNum].values, label=dataLab[yDataNum])
            axes[rowIdx].set_xticks(x[::xDispIval]) 
            axes[rowIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[rowIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[rowIdx].legend(ncol=legCol, fontsize=legFS, loc=legLoc)
            axes[rowIdx].grid(linestyle='--', linewidth=0.5)
            count += 1
            if count%groupNum == 0:
                rowIdx += 1
                count = 0
            else:
                continue

    else:
        for yDataNum in range(len(dataLab)):
            axes[rowIdx, colIdx].plot(x, y.iloc[:, yDataNum].values, label=dataLab[yDataNum])
            axes[rowIdx, colIdx].set_xticks(x[::xDispIval]) 
            axes[rowIdx, colIdx].tick_params(axis='x', labelsize=xTickFS)
            axes[rowIdx, colIdx].tick_params(axis='y', labelsize=yTickFS)
            axes[rowIdx, colIdx].legend(ncol=legCol, fontsize=legFS, loc=legLoc)
            axes[rowIdx, colIdx].grid(linestyle='--', linewidth=0.5)
            count += 1
            if count%groupNum == 0:
                colIdx += 1
                if colIdx % figColNum == 0:
                    rowIdx += 1
                    colIdx = 0
                    count = 0
                else:
                    continue
            else:
                continue
    
    fig.text(0.5, 0, xLabNam, ha='center', va='center', fontsize=xLabFS)
    fig.text(0.07, 0.5, yLabNam, ha='center', va='center', rotation='vertical', fontsize=yLabFS)
    fig.savefig(saveDir + saveNam, bbox_inches="tight")
    plt.close()
    return None


if __name__ == "__main__":
    saveDir = str(pathlib.Path(__file__).parent.resolve())

    # Demonstration
    dt = np.random.randint(-10, 10, (32, 5))
    df = pd.DataFrame(dt, columns=["A", "B", "C", "D", "E"])
    df_x = df.iloc[:, 0]
    df_y = df.iloc[:, [i for i in range(1, 5, 1)]]

    plotAll(df_x, df_y, "Val1", "Val2", df_y.columns, saveDir, "/testAll.jpg", xDispIval=10, legCol=2)
    plotEach(df_x, df_y, 2, 3, "Val1", df_y.columns, saveDir, "/testEach.jpg", xDispIval=10, xLabFS=18)
    plotEachGroup(df_x, df_y, 1, 2, 2, "Val1", "val2", df_y.columns, saveDir, "/testEachGroup.jpg", xDispIval=10, xLabFS=18, yLabFS=18)