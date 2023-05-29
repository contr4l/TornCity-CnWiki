import * as cal_func from "./calculator.js";

function format_num(num){
  if (num > 1e9){
    return (num / 1e9).toFixed(2) + 'b';
  }
  else if (num > 1e6){
    return (num / 1e6).toFixed(2) + 'm';
  }
  else if (num > 1e3){
    return (num / 1e3).toFixed(2) + 'k';
  }
  else {
    return num.toFixed(2);
  }
}

export class Exercise_Params {
  constructor() {
    console.log("Initializing Exercise_Params");
    this.reset_all_params();
    this.show_basic_info();
  }

  reset_all_params() {
    console.log("Reseting all params");
    this.initial_happiness = 5025;
    this.current_happiness = 5025;

    this.current_bonus = 1.0;

    this.start_gym_name = "Premier Fitness";
    // this.stop_gym_name = "Premier Fitness";
    this.stop_gym_name = "George's";
    this.current_gym_name = "Premier Fitness";

    this.current_focus = "def";

    this.current_gym_progress = 0;
    this.current_gym_limit = 0;

    this.current_stats = [0, 0, 0, 0];
    this.exercise_chain = new Array(["str"]);
    this.exercise_idx = 0;

    this.update_callback = null;
  }

  show_basic_info() {
    console.log(`start gym is ${this.start_gym_name}\
                   \nstop  gym is ${this.stop_gym_name} \
                   \ncurrent todo  is ${this.current_focus}\
                   \ncurrent perks is ${this.current_bonus}`);
    console.log(`current stats is \
      \nstr = ${this.current_stats[0].toFixed(2)}, \
      \ndef = ${this.current_stats[1].toFixed(2)}, \
      \nspd = ${this.current_stats[2].toFixed(2)}, \
      \ndex = ${this.current_stats[3].toFixed(2)}`);
  }

  stats_info() {
    return (
      this.current_stats[0].toFixed(2) +
      "," +
      this.current_stats[1].toFixed(2) +
      "," +
      this.current_stats[2].toFixed(2) +
      "," +
      this.current_stats[3].toFixed(2)
    );
  }
}

Exercise_Params.prototype.push_attr = function (stats_name) {
  this.exercise_chain.push(stats_name);
};

Exercise_Params.prototype.clear_attr = function () {
  this.exercise_chain = new Array();
};

Exercise_Params.prototype.last_attr = function () {
    if (this.exercise_chain.length === 0)
        return "str";

    return this.exercise_chain[this.exercise_chain.length - 1]
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
};

Exercise_Params.prototype.update = function (gym_idx, exercise_idx) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = this.exercise_chain[exercise_idx];
};

Exercise_Params.prototype.overall_greedy_update = function (
  gym_idx,
  exercise_idx
) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = cal_func.find_greedy_stats(
    gym_idx,
    this.current_stats,
    false
  );
  this.push_attr(this.current_focus);
};

Exercise_Params.prototype.strspd_greedy_update = function (
  gym_idx,
  exercise_idx
) {
  this.current_gym_name = cal_func.gym_name_list[gym_idx];
  this.current_focus = cal_func.find_greedy_stats(
    gym_idx,
    this.current_stats,
    true
  );
  this.push_attr(this.current_focus);
};

Exercise_Params.prototype.finish_train = function (gym_idx) {
  this.current_gym_progress = cal_func.gym_exp[gym_idx];
  this.current_gym_limit = cal_func.gym_exp[gym_idx];
};

// process_1: using the same happiness for the whole time
Exercise_Params.prototype.iter_process = function () {
  let gym_idx = cal_func.find_gym_idx(this.current_gym_name);

  while (!this.should_stop_iter()) {
    // Each iteration will finish one gym
    // this.update(gym_idx, this.exercise_idx);
    this.update_callback(gym_idx, this.exercise_idx);
    // console.log(
    //   `current gym change to ${this.current_gym_name}, focus changed to ${this.current_focus}`
    // );

    let train_times = cal_func.get_total_train_times(gym_idx);
    let stats_idx = cal_func.stats_idx_map[this.current_focus];

    // console.log(`train_times: ${train_times}`);
    for (let i = 0; i < train_times; i++) {
      this.current_stats[stats_idx] += cal_func.single_train_gains(
        this.current_focus,
        this.current_gym_name,
        this.current_stats[stats_idx],
        this.current_happiness,
        this.current_bonus
      );
    }
    // console.log(this.current_focus, this.current_gym_name, this.current_stats[stats_idx].toFixed(2), this.current_happiness, this.current_bonus);

    console.log(
      `finish ${this.current_gym_name}, stats changed to ${this.stats_info()}`
    );
    // hit the stop condition
    this.finish_train(gym_idx);
    gym_idx += 1;
  }
  console.log("train order is ", this.exercise_chain);
};

Exercise_Params.prototype.render_result = function () {
  console.log(`after exercise from ${this.start_gym_name} to ${
    this.stop_gym_name
  },\
      \nyour stats is \
      \nstr = ${format_num(this.current_stats[0])}, \
      \ndef = ${format_num(this.current_stats[1])}, \
      \nspd = ${format_num(this.current_stats[2])}, \
      \ndex = ${format_num(this.current_stats[3])}`);

    let str_result = document.getElementById("str_label");
    let def_result = document.getElementById("def_label");
    let spd_result = document.getElementById("spd_label");
    let dex_result = document.getElementById("dex_label");

    str_result.textContent = format_num(this.current_stats[0]);
    def_result.textContent = format_num(this.current_stats[1]);
    spd_result.textContent = format_num(this.current_stats[2]);
    dex_result.textContent = format_num(this.current_stats[3]);
};

var PRESET_SELECTOR_USER_DEFINED = 0;
var PRESET_SELECTOR_GREEDY_OVERALL = 1;
var PRESET_SELECTOR_GREEDY_STR_SPD = 2;
Exercise_Params.prototype.read_preset = function () {
  let element = document.getElementById("preset_selector");
  if (element.selectedIndex == PRESET_SELECTOR_USER_DEFINED) {
    this.update_callback = this.update;
    return false;
  } else if (element.selectedIndex == PRESET_SELECTOR_GREEDY_OVERALL) {
    console.log("PRESET_SELECTOR_GREEDY_OVERALL is selected");
    this.update_callback = this.overall_greedy_update;
  } else if (element.selectedIndex == PRESET_SELECTOR_GREEDY_STR_SPD) {
    console.log("PRESET_SELECTOR_GREEDY_STR_SPD is selected");
    this.update_callback = this.strspd_greedy_update;
  }
  return true;
};

Exercise_Params.prototype.get_exercise_chain = function () {
  this.clear_attr();
  document.querySelectorAll(".attr_select").forEach((element) => {
    let idx = element.selectedIndex;
    if (element.options[idx].text == "same as above") {
      this.push_attr(this.last_attr());
    } else if (element.options[idx].text == "PRESET") {
      alert("PRESET not compatiable with User Defined, the result would be incorrect");
      return;
    }
    else {
      this.push_attr(element.options[idx].text);
    }
  });
  // console.log(this.exercise_chain);
};

Exercise_Params.prototype.get_start_stop_gym = function () {
  document.querySelectorAll(".gym_row").forEach((element) => {
    // console.log("check", element.querySelector('td').textContent);
    if (element.querySelector('input[name="start_opt"').checked) {
      this.start_gym_name = element.querySelector("td").textContent;
    }
    if (element.querySelector('input[name="stop_opt"').checked) {
      this.stop_gym_name = element.querySelector("td").textContent;
    }
  });
};

Exercise_Params.prototype.get_initial_stats = function () {
  this.current_stats[0] = Number(document.getElementById('str_input').value);
  this.current_stats[1] = Number(document.getElementById('def_input').value);
  this.current_stats[2] = Number(document.getElementById('spd_input').value);
  this.current_stats[3] = Number(document.getElementById('dex_input').value);
};

function parse_perks(percentage) {
  if (isNaN(percentage) || Number(faction_perks) == 0) {
    return 1;
  }
  return 1 + Number(percentage / 100);
}

Exercise_Params.prototype.get_other_perks = function () {
  let faction_perks = document.getElementById('faction_perks').value;
  let property_perks = document.getElementById('property_perks').value;

  console.log("faction_perks = " + faction_perks, "property_perks = " + property_perks);

  this.current_bonus *= parse_perks(faction_perks);
  this.current_bonus *= parse_perks(property_perks);
};

Exercise_Params.prototype.read_params = function () {
  // when "start" button is clicked, read all params set from webpage
  // and start simulation

  // Step 1: get exercise chain
  if (!this.read_preset()) {
    this.get_exercise_chain();
  }

  // Step 2: get start and stop gym name
  this.get_start_stop_gym();

  // Step 3: get initial stats
  this.get_initial_stats();

  // Step 4: get bonus perks
  this.get_other_perks();
};
