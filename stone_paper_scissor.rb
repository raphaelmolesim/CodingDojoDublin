class StonePaperScissor

	@@lookup = {
		[:stone, :scissor] => :left_wins,
		[:stone, :paper] => :right_wins,

		[:paper, :scissor] => :right_wins,
		[:paper, :stone] => :left_wins,

		[:scissor, :stone] => :right_wins,
		[:scissor, :paper] => :left_wins,
	}

    def play(first, second)
		@@lookup[[first, second]] || :draw
    end
end
