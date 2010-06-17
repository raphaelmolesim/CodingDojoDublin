class StonePaperScissor

	@@rules = {
		[:stone, :scissor] => :left_wins,
		[:stone, :paper] => :right_wins,

		[:paper, :scissor] => :right_wins,
		[:paper, :stone] => :left_wins,

		[:scissor, :stone] => :right_wins,
		[:scissor, :paper] => :left_wins,
	}

    def play(player_one, player_two)
		@@rules.fetch [player_one, player_two], :draw
    end
end
