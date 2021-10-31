// copyright (c) by suhailvs
function funCreateFolder(ajaxurl,redirect){
	Alertify.dialog.prompt("Please enter a name for the new Folder.", function (str) {
		//if (str!=null){
        if (str.length>2 && str.length<21){
        	$.ajax({
			  type: "GET",
			  url: ajaxurl,
			  data: { folder:str }
			}).done(function(data){
			    if (data.flag=='0')Alertify.log.error(data.msg);
			    else
			    {
			    	if (redirect=='n'){
			    		$('#chznfolder').prop('selectedIndex',0);
			        	$('#chznfolder').append("<option value="+data.msg+" selected>"+str+"</option>");
			        	$('#chznfolder').trigger("chosen:updated");
			        	Alertify.log.success('Folder created successfully.');			    		
			    	}else{
			    		var url=redirect+'?curfolder='+str;
			    		document.location.href=url;
				    	//$('#ajaxBox').load(url);  
			        }
			    }		    
			});        	
            //document.location.href="{% url 'home' %}?folder="+folder;
        }else{
            Alertify.dialog.alert("The Folder name must be between 3 and 20 characters.");
        }
	}, function () {
		Alertify.log.error("Cancelled.");
    // user clicked "cancel"
	}, "miscellaneous");   
}

function funCreateTag(ajaxurl,redirect){
	Alertify.dialog.prompt("Please enter a name for the new Tag.", function (str) {
		//if (str!=null){
        if (str.length>2 && str.length<21){        	
        	$.ajax({
			  type: "GET",
			  url: ajaxurl,
			  data: { tag:str }
			}).done(function(data){
			    if (data.flag=='0')Alertify.log.error(data.msg);
			    else
			    {
			    	if (redirect=='n'){
			    		$('#chzntag').prop('selectedIndex',0);
			        	$('#chzntag').append("<option value="+data.msg+" selected>"+str+"</option>");
			        	$('#chzntag').trigger("chosen:updated");
			        	Alertify.log.success('Tag created successfully.');		    		
			    	}else{
			    		var url=redirect+'?curfolder='+str;
			    		document.location.href=url;
				    	//$('#ajaxBox').load(url);  
			        }
			    }		    
			});     
			
            //document.location.href="{% url 'home' %}?folder="+folder;
        }else{
            Alertify.dialog.alert("The Tag name must be between 3 and 20 characters.");
        }
	}, function () {
		Alertify.log.error("Cancelled.");
    // user clicked "cancel"
	});   
}