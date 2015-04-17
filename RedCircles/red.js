// 0 means to not output anything. Otherwise, output red__.png
function circlesize(var ff) {
	if (ff <= 0) {
		return 0;
	}
	r = (int) (Math.sqrt(ff)/10);
	if (r<5)
		return r+1;
	else if (r<9)
		return 7;
	else if (r<13)
		return 10;
	else if (r<18)
		return 15;
	else if (r<23)
		return 20;
	else if (r<28)
		return 25;
	else if (r<35)
		return 30;
	else
		return 40;
}