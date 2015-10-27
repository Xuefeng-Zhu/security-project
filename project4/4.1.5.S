.global _main
.section .data
shell:
	.asciz "/bin/sh\0"
.section .text

_main:

push    %ebp
mov     %esp,%ebp

subl $0x8, %esp
movl $shell, -0x8(%ebp)
movl $0, -0x4(%ebp)

mov $shell, %ebx
leal -0x8(%ebp), %ecx
mov $0, %edx
mov $11, %eax
int $0x80

leave
ret
