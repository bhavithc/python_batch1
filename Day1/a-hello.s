	.arch armv8-a
	.file	"hello.c"
	.text
	.section	.rodata
	.align	3
.LC0:
	.string	"HELLO"
	.align	3
.LC1:
	.string	"Hello world"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB0:
	.cfi_startproc
	stp	x29, x30, [sp, -32]!
	.cfi_def_cfa_offset 32
	.cfi_offset 29, -32
	.cfi_offset 30, -24
	mov	x29, sp
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	str	x0, [sp, 24]
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
	mov	w0, 0
	ldp	x29, x30, [sp], 32
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
