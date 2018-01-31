;(function(){
	'use strict';

	/*store.set('user', '桑笑楠');
    var user = store.get('user');
    console.log('user', user);*/
    // store.clear();

	var $add_task = $('.add-task'),
		$delete_task, //= $('.action.delete'), 在这里直接选择找不到，因为之后的数据是动态添加的，一开始是不存在，jq无法自动更新文档流
		$detail_task,
		$task_detail = $('.task-detail'),
		$task_detail_mask = $('.task-detail-mask'),
		current_index,
		$update_form,
		$task_detail_content,
		$task_detail_content_input,
		task_list = [];

	init();

	$add_task.on('submit', function(e){
		e.preventDefault();
		var $input = $(this).find('input[name=content]'),
			new_task = {};

		new_task.content = $input.val();
		// console.log(new_task);

		if(!new_task.content)	return;

		/*存入新Task*/
		if(addTask(new_task)) {
			/*更新页面任务列表*/
// 			render_task_list()
			/*清空输入框*/
			$input.val(null);
		}

	});

	$task_detail_mask.on('click', hide_task_detail);

	/*查找并监听所有删除按钮的点击事件*/
    function listen_task_delete() {
    	$delete_task.on('click', function() {
	    	var $this = $(this);
	    	var $item = $this.parent().parent();
	    	// console.log($item.data('index'));
	    	var tmp = confirm('确定删除？');
	    	tmp ? delete_task($item.data('index')) : null;
    	});
    }
    
    function listen_task_detail() {
    	$('.task-item').on('dblclick', function() {
    		var index = $(this).data('index');
            show_task_detail(index)
    	});

        $detail_task.on('click', function() {
            var $this = $(this);
            var $item = $this.parent().parent();
            var index = $item.data('index');
            // console.log(index)
            show_task_detail(index)
        });
    }

    function show_task_detail(index) {
    	render_task_detail(index);
    	current_index = index;
    	$task_detail.show();
    	$task_detail_mask.show();
    }

    function update_task(index, data) {
    	if(index === undefined || !task_list[index])
    		return;
    	task_list[index] = /*$.merge({}, task_list[index], */data;
    	refresh_task_list();
    }

    /*渲染指定Task的详细信息*/
    function render_task_detail(index) {
    	if(index === undefined || !task_list[index])
    		return;
    	var item = task_list[index];
    	var tpl = '<form>' +
            '<div class="content">' +
                item.content +
            '</div>' +
            '<div class="input-item">' + 
            '<input style="display:none" type="text" name="content" value="' + (item.content || '') + '">' + 
            '</div>' + 
            '<div>' +
                '<div class="desc input-item">' +
                    '<textarea name="desc">' + (item.desc || '') + '</textarea>' +
                '</div>' +
            '</div>' +
            '<div class="remind input-item">' +
                '<input name = "remind_date" type="date" value="' + item.remind_date + '">' +
            '</div>' +
            '<div class="input-item"><button type="submit">更新</button></div>' +
        '</form>';
        $task_detail.html(null);
        $task_detail.html(tpl);

        $update_form = $task_detail.find('form');
        $task_detail_content = $update_form.find('.content');
        $task_detail_content_input = $update_form.find('[name=content]');

        $task_detail_content.on('dblclick', function() {
        	$task_detail_content_input.show();
        	$task_detail_content.hide();
        });

        $update_form.on('submit', function(e) {
        	e.preventDefault();
        	var data = {};
        	data.content = $(this).find('[name=content]').val();
        	data.desc = $(this).find('[name=desc]').val();
        	data.remind_date = $(this).find('[name=remind_date]').val();
        	// console.log(data);
        	update_task(index, data);

        	hide_task_detail();
        })
    }

    function hide_task_detail() {
    	$task_detail.hide();
    	$task_detail_mask.hide();
    }

	function init() {
		task_list = store.get('task_list') || [];
		render_task_list()
	}
    
    /*刷新localstorage数据并渲染模板*/
    function refresh_task_list() {
        store.set('task_list', task_list);
        render_task_list();
    }
    
	function addTask(new_task) {
		task_list.push(new_task);
		refresh_task_list();
		return true;
		// console.log(task_list);
	}
    
    /*删除一条task*/
    function delete_task(index) {
        /*如果没有index，或者index在task_list中不存在*/
        if(index === undefined || !task_list[index]) return;
        
        delete task_list[index];
        refresh_task_list();
    }
    
    /*渲染所有Task模板*/
	function render_task_list() {
		var $task_list = $('.task-list');
		$task_list.html('');
		for(var i = 0; i < task_list.length; i++) {
			var $task = render_task_item(task_list[i], i);
			// console.log($task);
			$task_list.prepend($task);
		}
		$delete_task = $('.action.delete');
		$detail_task = $('.action.detail');
		listen_task_delete();
		listen_task_detail();
	}

	/*渲染单条Task模板*/
	function render_task_item(data, index) {
		if(!data || index === undefined)	return;
		var list_item_tpl = 
			'<div class="task-item" data-index="' + index + '">' +
            '<span><input type="checkbox"></span>' + 
            '<span class="task-content">' + data.content + '</span>' + 
            '<span class="float-right">' + 
            '<span class="action delete"> 删除</span>' + 
            '<span class="action detail"> 详细</span>' + 
            '</span>' + 
            '</div>';
        // console.log(list_item_tpl);
        return $(list_item_tpl);
	}

})();