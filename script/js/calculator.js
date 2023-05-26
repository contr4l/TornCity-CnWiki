
var light_dots = [
    [2.0, 2.0, 2.0, 2.0],
    [2.4, 2.4, 2.7, 2.4],
    [2.7, 3.2, 3.0, 2.7],
    [3.2, 3.2, 3.2, NaN],
    [3.4, 3.6, 3.4, 3.2],
    [3.4, 3.6, 3.6, 3.8],
    [3.7, NaN, 3.7, 3.7],
    [4.0, 4.0, 4.0, 4.0]
];

var middle_dots = [
    [4.8, 4.4, 4.0, 4.2],
    [4.4, 4.6, 4.8, 4.4],
    [5.0, 4.6, 5.2, 4.6],
    [5.0, 5.2, 5.0, 5.0],
    [5.0, 5.4, 4.8, 5.2],
    [5.5, 5.7, 5.5, 5.2],
    [NaN, 5.5, 5.5, 5.7],
    [6.0, 6.0, 6.0, 6.0]
]

var heavy_dots = [
    [6.0, 6.2, 6.4, 6.2],
    [6.5, 6.4, 6.2, 6.2],
    [6.4, 6.5, 6.4, 6.8],
    [6.4, 6.4, 6.8, 7.0],
    [7.0, 6.4, 6.4, 6.5],
    [6.8, 6.5, 7.0, 6.5],
    [6.8, 7.0, 7.0, 6.8],
    [7.3, 7.3, 7.3, 7.]
]

var special_dots = [
    [NaN, NaN, 7.5, 7.5],
    [7.5, 7.5, NaN, NaN],
    [8.0, NaN, NaN, NaN],
    [NaN, NaN, 8.0, NaN],
    [NaN, 8.0, NaN, NaN],
    [NaN, NaN, NaN, 8.0],
    [9.0, 9.0, 9.0, 9.0],
    [10.0, 10.0, 10.0, 10.0]
]

var special_energy_per_train_list = [
    25, 25, 50, 50, 50, 50, 25, 10
]

var STR = 0, DEF = 1, SPD = 2, DEX = 3;
var SOFT_CAP = 50000000;
var LIGHT_IDX  = light_dots.length;
var MIDDLE_IDX = LIGHT_IDX + middle_dots.length;
var HEAVY_IDX  = MIDDLE_IDX + heavy_dots.length;

var all_gyms_dots = light_dots.concat(middle_dots)
                              .concat(heavy_dots)
                              .concat(special_dots);

var A_list = [1600, 1600, 1800, 2100];
var B_list = [1700, 2000, 1500, -600];
var C_list = [700,  1350, 1000, 1500];

/*************** 以下为对外提供的变量常量 ****************/ 
export const gym_name_list = [
    // light
    "Premier Fitness", "Average Joes", "Woody's Workout", "Beach Bods", "Silver Gym", "Pour Femme", "Davies Den", "Global Gym",

    // middle
    "Knuckle Heads", "Pioneer Fitness", "Anabolic Anomalies", "Core", "Racing Fitness", "Complete Cardio", "Legs, Bums and Tums", "Deep Burn",

    // heavy
    "Apollo Gym", "Gun Shop", "Force Training", "Cha Cha's", "Atlas", "Last Round", "The Edge", "George's",

    // special
    "Balboas Gym", "Frontline Fitness", "Gym 3000", "Mr. Isoyamas", "Total Rebound", "Elites", "The Sports Science Lab",    "Fight Club"
]

export const gym_exp = [
    200, 500, 1000, 2000, 2750, 3000, 3500, 4000, // light
    6000, 7000, 8000, 11000, 12420, 18000, 18100, 24140, // middle
    31260, 36610, 46640, 56520, 67775, 84535, 106305, 200000, // heavy
    NaN, NaN, NaN, NaN, NaN, NaN, NaN, NaN // special
]

export const stats_idx_map = {"str":STR, "def":DEF, "spd":SPD, "dex":DEX};


function new_round(n, m) {
    // round n to m decimals
    return Math.round(n * Math.pow(10, m)) / Math.pow(10, m) ;
}

function soft_cap(current_stats) {
    return SOFT_CAP + (current_stats - SOFT_CAP) / (8.77635 * Math.log10(current_stats))
}

function valdr_formula(C3, D3, K3, H3, G3, A, B)
{
    // C3 = gym dots
    // D3 = Energy per Train
    // K3 = Bonus Multiplier
    // H3 = current_stats
    // G3 = Happy
    // =(1/200000)*C3*D3*(K3)*(IF(H3<50000000,H3,(H3-50000000)/(8.77635*LOG(H3))+50000000)*ROUND(1+0.07*ROUND(LN(1+G3/250),4),4)+8*G3^1.05+VLOOKUP(B3,Sheet2!K1:M4,2,FALSE)*(1-(G3/99999)^2)+VLOOKUP(B3,Sheet2!K1:M4,3,FALSE))
    // console.log(`C3=${C3}, D3=${D3}, K3=${K3}, H3=${H3}, G3=${G3}, A=${A}, B=${B}`);

    let gains = 1;
    gains = gains * 1 / 200000;
    gains = gains * C3 * D3 * K3;

    let Sp = H3 * new_round(1 + 0.07 * new_round(Math.log(1 + G3 / 250), 4), 4);
    Sp = Sp + 8 * Math.pow(G3, 1.05);
    Sp = Sp + (1 - Math.pow(G3 / 99999, 2)) * A;
    Sp = Sp + B;
   
    // console.log(`gains = ${gains}, Sp = ${Sp}`);
    gains = gains * Sp;
    // console.log(`current_stats is ${H3}, gains = ${gains}`);
    return gains;
}

/*************** 以下为对外提供函数接口 ****************/ 
export function find_gym_idx(input_gym_name)
{
    let gym_idx = 0;
    for (; gym_idx < gym_name_list.length; gym_idx++)
    {
        if (gym_name_list[gym_idx] == input_gym_name)
            break;
    }
    return gym_idx;
}

export function get_energy_per_train(gym_idx) {
    let energy_per_train = 0;

    if (gym_idx < LIGHT_IDX) {
        energy_per_train = 5;
    } else if (gym_idx < HEAVY_IDX) {
        energy_per_train = 10;
    } else {
        energy_per_train = special_energy_per_train_list[gym_idx - HEAVY_IDX];
    }
    return energy_per_train;
}

export function get_total_train_times(gym_idx) {
    let energy_per_train = get_energy_per_train(gym_idx);
    let total_energy_req = gym_exp[gym_idx];
    return Math.ceil(total_energy_req / energy_per_train); 
}

export function single_train_gains(stats_name, input_gym_name, current_stats, current_happy, current_bonus)
{
    let gym_idx = find_gym_idx(input_gym_name);
    if (gym_idx == gym_name_list.length){
        console.log("Invalid gym name input");
        return NaN;
    }

    let stats_idx = stats_idx_map[stats_name];

    // Initial co-efficiency
    // C3
    let gym_dots = all_gyms_dots[gym_idx][stats_idx];
    
    // D3
    let energy_per_train = get_energy_per_train(gym_idx);
    
    current_stats = current_stats < SOFT_CAP ? current_stats : soft_cap(current_stats);

    let A = A_list[stats_idx], B = B_list[stats_idx];

    let gains = valdr_formula(gym_dots, energy_per_train,
                              current_bonus, current_stats, current_happy, 
                              A, B);
    
    return gains;
}

