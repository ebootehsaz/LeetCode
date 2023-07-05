CXX := g++
CXXFLAGS := -std=c++11
BIN_DIR := bin

SRCS := $(wildcard *.cpp)
OBJS := $(SRCS:.cpp=.o)
EXECS := $(SRCS:.cpp=)

.PHONY: all clean

all: $(EXECS)

$(EXECS): %: %.o
	@echo "Linking $@..."
	$(CXX) $(CXXFLAGS) $< -o $(BIN_DIR)/$@

%.o: %.cpp
	@echo "Compiling $@..."
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(BIN_DIR)/%: %.cpp
	@echo "Building $@..."
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	@echo "Cleaning up..."
	rm -rf $(BIN_DIR)/*.o $(BIN_DIR)/$(EXECS)
