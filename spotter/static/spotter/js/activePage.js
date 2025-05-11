const pathName = window.location.pathname;
//const pageName = pathName.split('/').pop().replace('.html', '');

const b = pathName.split('/')[1]
const pageName = b

if (pageName === '%2Fspotter'){
	document.querySelector(".home1").classList.add("active")
}

if (pageName === '%2Fdownload'){
	document.querySelector(".home4").classList.add("active")
}