@echo off

echo "Stick firmware app builder"
tar -cf app.stk --format=zip --options="zip:compression=store" -C app *
pause
