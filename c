#include <stdio.h>
#include <string.h>

void secret_function() {
    printf("You have triggered the secret function!\n");
}

void vulnerable_function() {
    char buffer[64];  // 64바이트의 버퍼
    printf("Enter some text: ");
    gets(buffer);  // gets 함수 사용하여 버퍼 오버플로우 가능하게 함
}

int main() {
    vulnerable_function();
    return 0;
}
