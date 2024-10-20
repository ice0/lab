all: segv

segv: segv.c segv.entitlements
	clang -g segv.c -o segv
	codesign -s - -f --entitlements segv.entitlements segv

segv.entitlements:
	/usr/libexec/PlistBuddy -c "Add :com.apple.security.get-task-allow bool true" segv.entitlements

clean:
	rm segv
	rm segv.entitlements
	rm -rf segv.dSYM
