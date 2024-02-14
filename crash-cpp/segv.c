// https://nasa.github.io/trick/howto_guides/How-to-dump-core-file-on-MacOS.html

int main() {
    int *p = (void*)0;
    *p = 0;
    return 0;
}
