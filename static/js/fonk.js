function channels(network){

    var url ="/get_channels/" + network;

    $.get(url, function(data){
	    $( "#channels_list" ).empty().append(data);
	}
	);
}
function programs(channel){

    var url ="/get_programs/" + channel;

    $.get(url, function(data){
	    $( "#programs_list" ).empty().append(data);
	}
	);
}
function videos(program){

    var url ="/get_videos/" + program;

    $.get(url, function(data){
	    $( "#videos_list" ).empty().append(data);
	}
	);
}
