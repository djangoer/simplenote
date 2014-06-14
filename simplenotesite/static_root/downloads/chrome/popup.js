function loadforms(data){
	if (data.response.islogin=='yes'){		
		$('#frmnote').show();
		$('#login').hide();
		$("#cmbtag").empty();
		jQuery.each(data.response.taglist, function() {
			$('#cmbtag').append('<option value="'+this+'">'+this+'</option>');
		});
		$("#cmbfolder").empty();
		jQuery.each(data.response.folderlist, function() {
			$('#cmbfolder').append('<option value="'+this+'">'+this+'</option>');
		});
		$("#cmbfolder").chosen({disable_search_threshold: 5});
		$("#cmbtag").chosen({disable_search_threshold: 5});
	}else if (data.response.islogin=='no'){
		//alert('dont show notes');
	 	$('#login').show();
		$('#frmnote').hide();
		$('#popup-error').text(data.response.msg);			
	}else if (data.status == 200 && data.response != null) { // notlogged in
		//alert('notlogged');
	}
}

function validateForm(tt,fol,note)
{	var note=note;
	var title=tt;
	var folder=fol;
	var message='';
	if (title.length<5)message='Title must have atleast 5 characters.';
	else if (note.length<10)message='Note must have atleast 10 characters.';
	else if (!folder)message="Please Select a Folder.";
	if (message){
		alert(message);		
		return false;
	}
	else{
		return true;
	}	
}

var XhrSaveNote = {
	init: function() {
		$('#frmnote').submit(function(event){
			event.preventDefault();
			XhrSaveNote.noteSave();
		});
	},
	noteSave: function() {
		var title=$('#popup-title').val();
		var folder=$('#cmbfolder').val();
		var note=$('#popup-note').val();
		var frmclean=validateForm(title,folder,note);
		if (frmclean){
			var details = {
				url: 'http://try.simplenote.in/ext/',
				method: 'POST',
				async: true,
				params: {
					'title':title,
					'folder':folder,
					'note':note,
					'tag':$("#cmbtag").val()
					},
				contentType: 'text'
			};
			kango.xhr.send(details, function(data) {
				//$('#popup-error').text((data.status == 200 && data.response != null) ? data.response : 'Error. Status=' + data.status);
				$('#popup-error').text(data.response);
				alert(data.response);
				KangoAPI.closeWindow();
				//$('#frmnote').reset();
			});
		}
	}
};
var XhrLogin = {
	init: function() {
		$('#frmlogin').submit(function(event){
			event.preventDefault();
			XhrLogin.auth();
		});
	},
	auth: function() {
		var details = {
			url: 'http://try.simplenote.in/ext/',
			method: 'POST',
			async: true,
			params: {
				'username':$('#popup-user').val(),
				'password':$('#popup-pass').val()				
			},
			contentType: 'json',
			dataType:'json'			
		};
		kango.xhr.send(details, function(dt) {
			//$('#popup-error').text((data.status == 200 && data.response != null) ? data.response : 'Error. Status=' + data.status);
			loadforms(dt);
		});
	} 
};

KangoAPI.onReady(function() {
	//Check whether the user is logged in
	var logindetails = {
		url: 'http://try.simplenote.in/ext/',
		method: 'POST',
		async: true,
		params: {'type':'login'},
		contentType: 'json',
		dataType:'json'
	};
	XhrLogin.init();
	kango.xhr.send(logindetails, function(dt) {
		loadforms(dt);
	});
	//---- end login check---------------------
	
	XhrSaveNote.init();	
	$('#popup-close').click(function(event) {
		KangoAPI.closeWindow()
	});	
});