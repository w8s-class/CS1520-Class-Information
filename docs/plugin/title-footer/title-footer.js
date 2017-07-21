/********************************************************
*                                                       *
* Javascript for the Title-Footer plugin for Reveal.js  *
*                                                       *
* Author: Igor Leturia                                  *
*                                                       *
* License: GPL v3                                       *
* http://www.gnu.org/copyleft/gpl.html        *
*                                                       *
********************************************************/

/* Title-Footer object and properties declaration with default values */

var title_footer=
{
	title: '',
	details: [],
	background:'rgba(0,0,0,0.1)',
};

/* Function to obtain all child elements with any of the indicated tags (from http://www.quirksmode.org/dom/getElementsByTagNames.html) */

title_footer.getElementsByTagNames=function(list,obj)
{
	if (!obj)
	{
		var obj=document;
	};
	var tagNames=list.split(',');
	var resultArray=new Array();
	for (var i=0;i<tagNames.length;i++)
	{
		var tags=obj.getElementsByTagName(tagNames[i]);
		for (var j=0;j<tags.length;j++)
		{
			resultArray.push(tags[j]);
		};
	};
	var testNode=resultArray[0];
	if (!testNode)
	{
		return [];
	};
	if (testNode.sourceIndex)
	{
		resultArray.sort(
			function (a,b)
			{
				return a.sourceIndex-b.sourceIndex;
			}
		);
	}
	else if (testNode.compareDocumentPosition)
	{
		resultArray.sort(
			function (a,b)
			{
				return 3-(a.compareDocumentPosition(b)&6);
			}
		);
	};
	return resultArray;
};

/* Method to initialize the Title-Footer footer */

title_footer.initialize=function(parameters)
{

	// Link to the Title-Footer CSS

	var link=document.createElement("link");
	link.href="plugin/title-footer/title-footer.css";
	link.type="text/css";
	link.rel="stylesheet";
	document.getElementsByTagName("head")[0].appendChild(link);

	// Initialize properties according to parameters

	this.background=parameters.background || 'rgba(0,0,0,0.1)';
	this.details=parameters.details || [];
	var title=parameters.title || '';
	if (title!='')
	{
		this.title=title;
	}
	else
	{
		var first_section=document.getElementsByTagName('section')[0];
		if (first_section.getElementsByTagName('section').length>0)
		{
			first_section=first_section.getElementsByTagName('section')[0];
		};
		var title_elements=this.getElementsByTagNames('h1,h2,h3',first_section);
		if (title_elements.length>0)
		{
			this.title=title_elements[0].textContent;
			for (var title_elements_index=1;title_elements_index<title_elements.length;title_elements_index++)
			{
				this.title=this.title+' - '+title_elements[title_elements_index].textContent;
			};
		};
	};

	// Create the Title-Footer footer

	var title_footer=document.createElement('footer');
	title_footer.setAttribute('id','title-footer');
	title_footer.setAttribute('style','background:'+this.background);
	
	var title_footer_ul=document.createElement('ul');
	title_footer.appendChild(title_footer_ul);

	var title_item_element = document.createElement('li');

	var a_element=document.createElement('a');
	a_element.setAttribute('href','#/0');
	a_element.appendChild(document.createTextNode(this.title));
	title_item_element.appendChild(a_element);

	title_footer_ul.appendChild(title_item_element);
	
	if (this.details.length > 0) {
		for (var i = 0; i < this.details.length; i++) {
		    var item_element = document.createElement('li');
		    if (this.details[i].link) {
			    var item_link_element = document.createElement('a');
			    item_link_element.setAttribute('href',this.details[i].link);
			    item_link_element.setAttribute('target','_blank');
			    item_link_element.appendChild(document.createTextNode(this.details[i].text));
			    item_element.appendChild(item_link_element);
			} else {
				item_element.appendChild(document.createTextNode(this.details[i].text));
			}
		    title_footer_ul.appendChild(item_element);
		}
	} 
	
	var div_class_reveal=document.querySelectorAll('.reveal')[0];
	div_class_reveal.appendChild(title_footer);
};

