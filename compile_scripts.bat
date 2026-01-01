@ECHO OFF

CD Scripts

luac -s SWinEff.lua

IF EXIST SWinEff.lur (
  DEL SWinEff.lur
)

RENAME luac.out SWinEff.lur

@REM ----------------------------------------------------------------------------

CD AreaScripts

luac -s Bdorm.lua

IF EXIST Bdorm.lur (
  DEL Bdorm.lur
)

RENAME luac.out Bdorm.lur

REM ----------------------------------------------------------------------------

CD ../../

MOVE Scripts\SWinEff.lur _build\Scripts\
MOVE Scripts\AreaScripts\Bdorm.lur _build\Scripts\AreaScripts\
