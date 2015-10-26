.global _main
.section .data
command:
	.asciz "/bin/sh\0"
.section .text
argument:
	.asciz "-i\0"
_main:

push	%ebp
mov	%esp,%ebp
subl $12, %esp

movl $command, %esp
movl $argument, 4(%esp)
movl $0, 8(%esp)

movl $11, %eax
movl $command, %ebx
leal 0(%esp), %ecx
movl $0, %edx
int $0x80

leave
ret