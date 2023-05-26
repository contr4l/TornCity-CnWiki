import * as cal_func from "./calculator.js";

class Exercise_Params {
  constructor() {
    this.reset_all_params();
  }

  reset_all_params() {
    console.log("Initializeing");
    this.initial_happiness = 5025;
    this.current_happiness = 5025;

    this.current_bonus = 1.0;

    this.start_gym_name = "Premier Fitness";
    this.stop_gym_name = "Premier Fitness";
    // this.stop_gym_name = "George's";
    this.current_gym_name = "Premier Fitness";

    this.current_focus = "str";

    this.current_gym_progress = 0;
    this.current_gym_limit = 0;

    this.current_stats = [0, 0, 0, 0];
    this.exercise_chain = new Array(["str"]);
    this.exercise_idx = 0;
  }

  show_basic_info() {
    console.log(`start gym is ${this.start_gym_name}\
                 \nstop  gym is ${this.stop_gym_name} \
                 \ncurrent stats is ${this.current_stats}\
                 \ncurrent todo  is ${this.current_focus}`);
  }
}

Exercise_Params.prototype.push_attr = function (stats_name) {
  this.exercise_chain.push(stats_name);
};

Exercise_Params.prototype.clear_attr = function () {
  this.exercise_chain = new Array();
};

Exercise_Params.prototype.validation_range = function () {
  start_idx = cal_func.find_gym_idx(this.start_gym_name);
  stop_idx = cal_func.find_gym_idx(this.stop_gym_name);

  return stop_idx - start_idx + 1 == this.exercise_chain.length;
};

Exercise_Params.prototype.set_happiness = function (h) {
  this.initial_happiness = h;
};

Exercise_Params.prototype.should_stop_iter = function () {
  // console.log(`current gym is ${this.current_gym_name}\
  //            \ntarget gym is ${this.stop_gym_name}`);
  // console.log(`current progress is ${this.current_gym_progress}, target progress is ${this.current_gym_limit}`);
  return (
    this.current_gym_name == this.stop_gym_name &&
    this.current_gym_progress >= this.current_gym_limit
  );
};

Exercise_Params.prototype.initialize = function () {
  this.current_gym_name = this.start_gym_name;
  this.current_focus = this.exercise_chain[0];
  this.current_gym_progress = 0;

  let gym_idx = cal_func.find_gym_idx(this.current_gym_name);
  this.current_gym_limit = cal_func.gym_exp[gym_idx];

  // this.show_basic_info();
};

Exercise_Params.prototype.update = function (gym_idx, exercise_idx) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = this.exercise_chain[exercise_idx];

  console.log(`current gym change to ${this.current_gym_name}, focus changed to ${this.current_focus}`);
};

Exercise_Params.prototype.finish_train = function (gym_idx) {
  this.current_gym_progress = cal_func.gym_exp[gym_idx];
  this.current_gym_limit = cal_func.gym_exp[gym_idx];
};

// process_1: using the same happiness for the whole time
Exercise_Params.prototype.iter_process_1 = function () {
  let gym_idx = cal_func.find_gym_idx(this.current_gym_name);

  while (!this.should_stop_iter()) {
    // Each iteration will finish one gym
    this.update(gym_idx, this.exercise_idx);

    let train_times = cal_func.get_total_train_times(gym_idx);
    let stats_idx = cal_func.stats_idx_map[this.current_focus];

    console.log(`focus on ${this.current_focus}, stats_idx is ${stats_idx}`);
    console.log(`train_times: ${train_times}`);
    for (let i = 0; i < train_times; i++) {
      this.current_stats[stats_idx] += cal_func.single_train_gains(
        this.current_focus,
        this.current_gym_name,
        this.current_stats[stats_idx],
        this.current_happiness,
        this.current_bonus
      );
    }
    console.log(this.current_focus, this.current_gym_name, this.current_stats[stats_idx], this.current_happiness, this.current_bonus);

    console.log(`finish ${this.current_gym_name}, stats changed to ${this.current_stats}`);
    // hit the stop condition
    this.finish_train(gym_idx);

    gym_idx += 1;
  }
};

Exercise_Params.prototype.render_result = function () {
  console.log(`after exercise from ${this.start_gym_name} to ${this.stop_gym_name},\
    your stats is \
    str = ${this.current_stats[0]}, \
    def = ${this.current_stats[1]}, \
    spd = ${this.current_stats[2]}, \
    dex = ${this.current_stats[3]}`);
};

Exercise_Params.prototype.read_params = function () {
  // when "start" button is clicked, read all params set from webpage
  // and start simulation
};

function simulation_process(handle) {
  handle.read_params();
  handle.initialize();
  handle.iter_process_1();
  handle.render_result();
}

(function () {
  var handle = new Exercise_Params();
  var startButton = document.getElementById('start_btn');
  startButton.addEventListener('click', function () {
    console.log("Start Simulation!");
    handle.show_basic_info();
    simulation_process(handle);
  });

  var resetButton = document.getElementById('reset_btn');
  resetButton.addEventListener('click', function () {
    console.log("Reset Simulation Params!");
    handle.reset_all_params();
  });
  
})();
