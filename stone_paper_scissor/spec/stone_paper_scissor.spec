require 'stone_paper_scissor'

describe "StonePaperScissor" do
    before do 
      @game = StonePaperScissor.new 
       
    end

	it "should be able to create a instance" do
		@game.should be_a StonePaperScissor
	end

    it "should say that stone beats scissor" do
        @game.play(:stone, :scissor).should be == :left_wins
    end

    it "should say that scissor beats paper" do
       @game.play(:scissor, :paper).should be == :left_wins

    end

    it "should say that paper beats stone" do
        @game.play(:paper, :stone).should be == :left_wins
    end

    it "paper should fail for scissor" do
        @game.play(:paper, :scissor).should be == :right_wins
    end

	it "scissor should fail for stone" do
        @game.play(:scissor, :stone).should be == :right_wins
    end

	it "should score draw" do
		@game.play(:scissor, :scissor).should be == :draw
	end

	it "consecutive games are always the same" do
		@game.play(:scissor, :scissor).should be == :draw
		@game.play(:scissor, :scissor).should be == :draw
	end

end
