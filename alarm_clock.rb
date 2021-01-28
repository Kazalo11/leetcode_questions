alarms = { 
    Morning: "8:30",
    Gym: "16:30"

}

puts "Would you like to set an alarm, see what alarms you have, change an alarm, or delete an alarm"
choice = gets.chomp

case choice
when "set"
    puts "What would you like to call the alarm? "
    name = gets.chomp
    if alarm[name.to_sym].isnil?
        puts "When would you like to set the alarm for? "
        time = gets.chomp
        alarm[name.to_sym] = time
    else  
        puts "There is already an alarm with that name!"
       
    end
when "change"
    puts "What was your alarm called? "
    name = gets.chomp
    if alarm[name.to_sym].isnil?
        puts "There is no alarm under this name"
    else  
        puts "What would you like the new time to be? "
        time = gets.chomp
        alarm[name.to_sym] = time
    end
when "see"
    alarm.each {|name,time| puts "#{name} is set for #{time}"}

when "delete"
    puts "What is the alarm called"
    name = gets.chomp
    alarm[name.to_sym].isnil? ? (puts "This alarm does not exist") : alarm.delete(name.to_sym)
else
    puts "Error, you did not select one of the options"
end

