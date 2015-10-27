.global _main
.section .data
shell:
	.asciz "/bin/sh\0"
.section .text

_main:

push    %ebp
mov     %esp,%ebp

subl $8, %esp
movl $shell, 0(%esp)
movl $0, 4(%esp)

mov $11, %eax
mov $shell, %ebx
leal 0(%esp), %ecx
mov $0, %edx
int $0x80

leave
ret
